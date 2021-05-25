import pandas as pd 
import os
from paths import data_path 

ceevee = f"{data_path}/baci_three_all_guardcat.csv"
story_stats_output = os.path.dirname(__file__) + "/story_stats/"

df = pd.read_csv(ceevee)

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

### CUT DOWN TO ONLY PACIFIC COUNTRIES AS EXPORTERS

pac_df = df.loc[df['Exporting country'].isin(pacific)]
extrac_df = pac_df.loc[pac_df['Category'] != "Other"]

#### WORK OUT TOTAL PACIFIC EXPORTS PER CATEGORY


totals = extrac_df.groupby(['Category'])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()

# combo['Value of the trade flow (thousands current USD)'] = combo['Value of the trade flow (thousands current USD)'] * 1000

total_calcs = pd.DataFrame.from_records([{"Category": "Total", 
"Value of the trade flow (thousands current USD)": totals['Value of the trade flow (thousands current USD)'].sum(),
 "Quantity (in metric tons)": totals['Quantity (in metric tons)'].sum()}])
totals = totals.append(total_calcs)

with open(f"{story_stats_output}kickoff_category_totals.csv", "w") as f:
    totals.to_csv(f, index=False, header=True)

# print(totals.round())


### WORK OUT TOTAL EXPORTS PER COUNTRY

count = extrac_df.groupby(['Exporting country'])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()


with open(f"{story_stats_output}kickoff_country_totals.csv", "w") as f:
    count.to_csv(f, index=False, header=True)
# print(count.round())


### WORK OUT TOTAL EXPORTS PER COUNTRY PER CATEGORY

count_cat = extrac_df.groupby(['Exporting country', "Category"])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()

with open(f"{story_stats_output}kickoff_country_category.csv", "w") as f:
    count_cat.to_csv(f, index=False, header=True)

print(count.round())

# ### CALCULATE TOTAL PACIFIC EXPORTS OF EXTRACTIVES (TONNES AND USD)

# extrac_df = pac_df.loc[pac_df['Category'] != "Other"]

# extrac_tonnes = extrac_df['Quantity (in metric tons)'].sum()
# extrac_usd = extrac_df['Value of the trade flow (thousands current USD)'].sum() * 1000

# totes_tonnes = pac_df['Quantity (in metric tons)'].sum()
# totes_usd = pac_df['Value of the trade flow (thousands current USD)'].sum() * 1000

# # tonnes_per = (extrac_tonnes / totes_tonnes)* 100
# # usd_per = (extrac_usd / totes_usd)* 100


# print(f"Pacific total extractive tonnes exported: {extrac_tonnes.round()}")
# print("\n")
# print(f"Pacific total extractive USD exported: {extrac_usd.round()}")
# print("\n\n\n")
# print(f"Pacific total tonnes exported: {totes_tonnes.round()}")
# print("\n")
# print(f"Pacific total USD exported: {totes_usd.round()}")