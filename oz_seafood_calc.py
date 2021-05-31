import pandas as pd 
import os
from paths import data_path 

ceevee = f"{data_path}/baci_three_all_guardcat.csv"
story_stats_output = os.path.dirname(__file__) + "/story_stats/"

df = pd.read_csv(ceevee)

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

### CUT DOWN TO ONLY PACIFIC COUNTRIES AS EXPORTERS

pac_df = df.loc[df['Exporting country'].isin(pacific)]

pac_oz = pac_df.loc[pac_df['Importing country'] == "Australia"].copy()

# sea = pac_oz.loc[pac_oz['Category'] == "Seafood products"].copy()

# print(sea)
# print(sea['Quantity (in metric tons)'].sum())
# print(pac_df)

grouped = pac_oz.groupby(by="Category")["Value of the trade flow (thousands current USD)","Quantity (in metric tons)"].sum().reset_index()

print(grouped)