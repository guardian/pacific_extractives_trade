import pandas as pd
import os
from paths import data_path
pd.options.display.float_format = '{:.0f}'.format

ceevee = f"{data_path}/baci_three_all_guardcat.csv"

extract = os.path.dirname(__file__) + "/extracts/"

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

which = "Quantity (in metric tons)"

df = pd.read_csv(ceevee)
logs = df.loc[df['Category'] == "Wood products"]
png = logs.loc[logs['Exporting country'] == "Papua New Guinea"]

# "Value of the trade flow (thousands current USD)","Quantity (in metric tons)"
dollar_total = png["Value of the trade flow (thousands current USD)"].sum()
weight_total = png["Quantity (in metric tons)"].sum()



total_calcs = pd.DataFrame.from_records([{"Year": "2019", 
"Exporting country": "Papua New Guinea", "Importing country": "Total",
"Value of the trade flow (thousands current USD)": dollar_total,
 "Quantity (in metric tons)": weight_total, "Category": "Wood products"}])
totals = png.append(total_calcs)

totals = totals.groupby(by=["Year", 'Exporting country', 'Importing country', "Category"])["Value of the trade flow (thousands current USD)","Quantity (in metric tons)"].sum().reset_index()

totals = totals.sort_values(by=["Value of the trade flow (thousands current USD)","Quantity (in metric tons)"], ascending=False)

totals["Dollar %"] = (totals["Value of the trade flow (thousands current USD)"]/dollar_total)*100
totals['Weight %'] = (totals['Quantity (in metric tons)']/weight_total)*100

print(totals)