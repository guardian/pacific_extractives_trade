import pandas as pd 
import os
from paths import data_path 
pd.options.display.float_format = '{:.0f}'.format

ceevee = f"{data_path}/baci_three_all_guardcat.csv"

extract = os.path.dirname(__file__) + "/extracts/"


df = pd.read_csv(ceevee)
# print(df.columns)

metric = 'Quantity (in metric tons)'
# metric = 'Value of the trade flow (thousands current USD)'
# df[metric] = df[metric] * 1000

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

pacific = df.loc[df['Exporting country'].isin(pacific)]

pacific = pacific[['Exporting country', 'Importing country',metric, 'Category']]

grouped = pacific.groupby(by=['Importing country', 'Category'])[metric].sum().reset_index()

sorted = grouped.sort_values(by=['Importing country', metric], ascending=False)


include = ['China', "Japan", "Australia"]



final = sorted.loc[sorted['Importing country'].isin(include)]

print(final)



with open(f"{extract}china_piece_stats_{metric}.csv", "w") as f:
    final.to_csv(f, index=False, header=True)


# print(sorted.loc[sorted['Importing country'] == "China"].round())
# print(sorted.loc[sorted['Importing country'] == "Australia"].round())
# print(sorted.loc[sorted['Importing country'] == "Japan"].round())

# gold = df.loc[df['Importing country'].isin(['Australia', 'China'])]
# gold = df.loc[df['Importing country'].isin(['China'])]
# gold = gold.loc[gold['Category'] == 'Oil, metals and mineral products']
# gold = gold.loc[gold['Exporting country'].isin(pacific_countries)]
# grouped = gold.groupby(by='hs4')[metric].sum().reset_index()
# sorted = grouped.sort_values(by=metric, ascending=False)

# 

# print(gold['hs4'].unique())

# print(sorted)
# gold = gold.loc[gold['hs4'] == 7108]
# # gold = gold[['Importing country', 'hs4',metric]]
# grouped = gold.groupby(by=["Importing country"])[metric].sum().reset_index()
# print(grouped.round())
# print(gold)

# print(oz_gold)
# print(oz_gold.columns)
# print(oz_gold['hs2'].unique())
# print(oz_gold['hs4'].unique())