import pandas as pd  
import os
dir = os.path.dirname(__file__)

"""
Variable	Description
t	Year
k	Product category (HS 6-digit code)
i	Exporter (ISO 3-digit country code)
j	Importer (ISO 3-digit country code)
v	Value of the trade flow (in thousands current USD)
q	Quantity (in metric tons)"""

df = pd.read_csv(f'{dir}/init_data/RENAMED_COUNTRIES_Pacific_BACI_HS4_HS2_descriptions.csv')

seafood = [3, 16]
wood = [6, 44, 47, 94]
minerals = [26, 27, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]
# https://unstats.un.org/unsd/tradekb/Knowledgebase/50043/HS-2002-Classification-by-Section

seafood = [(x, "Seafood products") for x in seafood]
wood = [(x, "Wood products") for x in wood]
minerals = [(x, "Oil, metals and mineral products") for x in minerals]

reclassify_list = seafood + wood + minerals


### CREATE A CHINA IMPORTING VERSION

df['Importer binary'] = 'Rest of world'

df.loc[df['Importing country'] == 'China', 'Importer binary'] = 'China'

df['Category'] = 'Other'

for thing in reclassify_list:
    df.loc[df['hs2'] == thing[0], 'Category'] = thing[1]

#### df = df.loc[df['Category'].notnull()]

df = df[['Year', 'Exporting country', 'Importing country', 'Importer binary', 'Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)', 'hs2_description', 'Category']]

# with open(f'{dir}/cleaned_data/BACI_exports_four_categories.csv', 'w') as f:
#     df.to_csv(f, header=True, index=False)

# print(df)

# df = df.loc[df['Category'] != "Other"]


# with open(f'{dir}/cleaned_data/BACI_exports_three_categories.csv', 'w') as f:
#     df.to_csv(f, header=True, index=False)
# print(df)



#### GROUP DATA SET BY CATEGORY


# df = df.groupby(['Exporting country', 'Category'])["Value of the trade flow (thousands current USD)", "Quantity (in metric tons)"].sum()

# df = df.reset_index()

# wood_money_total = df.loc[df['Category'] == "Wood products"]['Value of the trade flow (thousands current USD)'].sum()
# wood_weight_total = df.loc[df['Category'] == "Wood products"]['Quantity (in metric tons)'].sum()

# fish_money_total = df.loc[df['Category'] == "Seafood products"]['Value of the trade flow (thousands current USD)'].sum()
# fish_weight_total = df.loc[df['Category'] == "Seafood products"]['Quantity (in metric tons)'].sum()

# mineral_money_total = df.loc[df['Category'] == "Oil, metals and mineral products"]['Value of the trade flow (thousands current USD)'].sum()
# mineral_weight_total = df.loc[df['Category'] == "Oil, metals and mineral products"]['Quantity (in metric tons)'].sum()

# other_money_total = df.loc[df['Category'] == "Other"]['Value of the trade flow (thousands current USD)'].sum()
# other_weight_total = df.loc[df['Category'] == "Other"]['Quantity (in metric tons)'].sum()

# wood_total = {"Exporting country": "Pacific Total", "Category": "Wood products", "Value of the trade flow (thousands current USD)": wood_money_total, "Quantity (in metric tons)":wood_weight_total}

# fish_total = {"Exporting country": "Pacific Total", "Category": "Seafood products", "Value of the trade flow (thousands current USD)": fish_money_total, "Quantity (in metric tons)": fish_weight_total}

# mineral_total = {"Exporting country": "Pacific Total", "Category": "Oil, metals and mineral products", "Value of the trade flow (thousands current USD)": mineral_money_total, "Quantity (in metric tons)": mineral_weight_total}

# other_total = {"Exporting country": "Pacific Total", "Category": "Other", "Value of the trade flow (thousands current USD)": other_money_total, "Quantity (in metric tons)": other_weight_total}

# df = df.append(wood_total, ignore_index=True)
# df = df.append(fish_total, ignore_index=True)
# df = df.append(mineral_total, ignore_index=True)
# df = df.append(other_total, ignore_index=True)


# with open(f'{dir}/cleaned_data/BACI_exports_category_grouped.csv', 'w') as f:
#     df.to_csv(f, header=True, index=False)





### GROUP DATA SET BY IMPORTER AND EXPORTER

# df = df.groupby(['Importer binary', "Category"])["Value of the trade flow (thousands current USD)", "Quantity (in metric tons)"].sum()

# df = df.reset_index()

# with open(f'{dir}/cleaned_data/BACI_exports_three_categories_china_row_grouped.csv', 'w') as f:
#     df.to_csv(f, header=True, index=False)




