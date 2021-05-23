import pandas as pd 
import os
from paths import data_path 

# data_path = os.path.dirname(__file__)
# ceevee = f"{data_path}/data/baci_two_all_guardcat.csv"
ceevee = f"{data_path}/baci_three_all_guardcat.csv"

df = pd.read_csv(ceevee)

def workout_percent_of_exports(frame, metric, category):
    print(f"\n\n Working it out for {category} \n\n")

    ### WORK OUT TOTAL EXPORTS PER COUNTRY

    df = frame

    total_exports = df.groupby(['Exporting country'])[metric].sum().reset_index()
    total_exports.rename(columns = {f"{metric}": "Total tonnes"}, inplace=True)

    ### WORK OUT TOTAL EXTRACTIVES EXPORTS PER COUNTRY

    df = frame.loc[frame['Category'] != "Other"]

    total_extractives = df.groupby(['Exporting country'])[metric].sum().reset_index()
    total_extractives.rename(columns = {f"{metric}": "Total extractives tonnes"}, inplace=True)

    ### WORK OUT CATEGORY EXTRACTIVES PER COUNTRY

    df = frame.loc[frame['Category'] == category]

    total_cat = df.groupby(['Exporting country'])[metric].sum().reset_index()
    total_cat.rename(columns = {f"{metric}": f"Total tonnes of {category}"}, inplace=True)

    ### 

    merged = total_cat.merge(total_extractives, on='Exporting country', how='left')

    merged = merged.merge(total_exports, on='Exporting country', how='left')

    merged[f"{category} percent of total"] = (merged[f"Total tonnes of {category}"]/merged["Total tonnes"]) * 100

    print(merged.round())





# which_good = "Oil, metals and mineral products"

# which_measure = 'Quantity (in metric tons)'

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

### CUT DOWN TO ONLY PACIFIC COUNTRIES AS EXPORTERS

pac_df = df.loc[df['Exporting country'].isin(pacific)]

# workout_percent_of_exports(pac_df, which_measure, which_good)

#### WORK OUT TOTAL PACIFIC EXPORTS PER CATEGORY

extrac_df = pac_df.loc[pac_df['Category'] != "Other"]
combo = extrac_df.groupby(['Category'])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()
# combo['Value of the trade flow (thousands current USD)'] = combo['Value of the trade flow (thousands current USD)'] * 1000
print(combo.round())
print(combo['Value of the trade flow (thousands current USD)'].sum())

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
