import pandas as pd 
import os
from paths import data_path 

pd.options.display.float_format = '{:.0f}'.format

ceevee = f"{data_path}/baci_three_all_guardcat.csv"
extract = os.path.dirname(__file__) + "/extracts/"

df = pd.read_csv(ceevee)

sol = df.loc[df['Exporting country'] == "Solomon Isds"]

grouped = sol.groupby(by=['Exporting country', 'Category'])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()


with open(f"{extract}solomon_logging_piece_stats.csv", "w") as f:
    grouped.to_csv(f, index=False, header=True)
    
print(grouped)