import pandas as pd 
import os
from paths import data_path

here = os.path.dirname(__file__)
ceevee = f"{data_path}/pac_baci_three_all_guardcat_hs6.csv"
extract = os.path.dirname(__file__) + "/extracts/"

df = pd.read_csv(ceevee)

sf = df.loc[df['Category'] == "Seafood products"]

total = {}

# print(sf.columns)

total = pd.DataFrame([["Pacific total", "Seafood products", sf['Value of the trade flow (thousands current USD)'].sum(), sf['Quantity (in metric tons)'].sum()]], 
columns=(["Exporting country","Category",'Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)']))

grouped = sf.groupby(by=['Exporting country', "Category"])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()

# print(grouped)
# print(total)

combo = grouped.append(total)

combo['$ Pct of Pacific'] = round((combo['Value of the trade flow (thousands current USD)']/sf['Value of the trade flow (thousands current USD)'].sum())*100,2)
combo['T Pct of Pacific'] = round((combo['Quantity (in metric tons)']/sf['Quantity (in metric tons)'].sum())*100,2)

# with open(f"{here}/pacific_fishing_exporters.csv", 'w') as f:
#     combo.to_csv(f, index=False, header=True)


importers = sf.groupby(by=['Importing country', "Category"])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()

imp_total = pd.DataFrame([["Pacific total", "Seafood products", importers['Value of the trade flow (thousands current USD)'].sum(), importers['Quantity (in metric tons)'].sum()]],
columns=(["Importing country","Category",'Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'])) 

importers = importers.sort_values(by="Quantity (in metric tons)", ascending=False)

combo2 = importers.append(imp_total)

combo2['$ Pct of Pacific'] = round((combo2['Value of the trade flow (thousands current USD)']/importers['Value of the trade flow (thousands current USD)'].sum())*100,2)
combo2['T Pct of Pacific'] = round((combo2['Quantity (in metric tons)']/importers['Quantity (in metric tons)'].sum())*100,2)

combo2['$ per t'] = round((combo2['Value of the trade flow (thousands current USD)']*1000)/combo2['Quantity (in metric tons)'],2)

# print(importers)
with open(f"{here}/pacific_fishing_importers.csv", 'w') as f:
    combo2.to_csv(f, index=False, header=True)
print(combo2)