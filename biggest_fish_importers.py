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

pacific = ['Kiribati']

# pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

pacific = df.loc[df['Exporting country'].isin(pacific)]

pacific = pacific.loc[pacific['Category'] == "Seafood products"]

pacific = pacific[['Exporting country', 'Importing country',metric, 'Category']]

grouped = pacific.groupby(by=['Importing country', 'Category'])[metric].sum().reset_index()

sorted = grouped.sort_values(by=metric, ascending=False)


print(sorted.loc[sorted['Importing country'] == "China"])


# with open(f"{extract}china_piece_fish_stats_{metric}.csv", "w") as f:
#     sorted.to_csv(f, index=False, header=True)