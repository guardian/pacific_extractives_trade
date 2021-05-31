import pandas as pd
import os
from paths import data_path
pd.options.display.float_format = '{:.0f}'.format

ceevee = f"{data_path}/baci_three_all_guardcat.csv"

extract = os.path.dirname(__file__) + "/extracts/"

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

which = "Quantity (in metric tons)"
# which = "Value of the trade flow (thousands current USD)"

df = pd.read_csv(ceevee)
df = df.loc[df['Category'] != "Other"]

pac_df = df.loc[df['Exporting country'].isin(pacific)]

df = pac_df[['Exporting country', 'Importing country',
'Value of the trade flow (thousands current USD)',
       'Quantity (in metric tons)', 'Category']]

customers = df.groupby(by=['Importing country'])['Quantity (in metric tons)'].sum().reset_index()
customers['Percent'] = (customers['Quantity (in metric tons)']/customers['Quantity (in metric tons)'].sum())*100
# seafood = pac_df.loc[pac_df['Category'] == "Seafood products"]['Quantity (in metric tons)'].sum()

customers = customers.sort_values(by="Quantity (in metric tons)", ascending=False)

print(customers.head(12))
# print(customers.columns)
# print(customers["Quantity (in metric tons)"].sum())
