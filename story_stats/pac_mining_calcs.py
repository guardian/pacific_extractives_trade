import pandas as pd 
import os
from paths import data_path

here = os.path.dirname(__file__)
# ceevee = f"{data_path}/pac_baci_three_all_guardcat_hs6.csv"
ceevee = f"{data_path}/baci_three_all_guardcat.csv"
# extract = os.path.dirname(__file__) + "/extracts/"

# # hs6_codes = 

df = pd.read_csv(ceevee)

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

### CUT DOWN TO ONLY PACIFIC COUNTRIES AS EXPORTERS

pac_df = df.loc[df['Exporting country'].isin(pacific)]
mining = pac_df.loc[pac_df['Category'] == "Oil, metals and mineral products"]
print(mining['Quantity (in metric tons)'].sum())


# codes = f"{data_path}/product_codes_HS17_V202102.csv"

# codes = pd.read_csv(codes)

# merged = pd.merge(df, codes, left_on="Product category", right_on="code", how="left")

# mining = merged.loc[merged['Category'] == "Oil, metals and mineral products"].copy()

# print(type(mining))

# # with open(f"{here}/pacific_mining_all.csv", 'w') as f:
# #     mining.to_csv(f, index=False, header=True)

# # print(mining['hs2'].unique())


# mining_cats = [(26, "Ores, slag and ash"), (27, "Mineral fuels, mineral oils and products of their distillation"), 
# (72,"Iron and steel"),  (73, "Articles of iron or steel"),
#  (74,"Copper and articles thereof"), (75,"Nickel and articles thereof"), 
#  (76,"Aluminium and articles thereof"), (78, "Lead and articles thereof"), 
#  (79, "Zinc and articles thereof"),
#  (80, "Tin and articles thereof"), (81, "Other base metals; cermets; articles thereof"), 
#  (83, "Miscellaneous articles of base metal")]


# listo = []

# for thing in mining_cats:


#     init_df = mining.loc[mining['hs2'] == thing[0]]
#     init_df['Product'] = thing[1]
#     # print(init_df)
#     listo.append(init_df)


# gold = mining.loc[mining['hs4'] == 7108].copy()
# gold['Product'] = "Gold"
# listo.append(gold)


# final = pd.concat(listo)

# final = final[['Year', 'Exporting country', 'Importing country', 'Product', 'Value of the trade flow (thousands current USD)',
#        'Quantity (in metric tons)', 'description', 'Product category',
#        'hs4', 'hs2']]

# with open(f"{here}/pacific_mining.csv", 'w') as f:
#     final.to_csv(f, index=False, header=True)


# grouped = final.groupby(by=["Importing country", "Product"])['Value of the trade flow (thousands current USD)',
#        'Quantity (in metric tons)'].sum()



# grouped = grouped.reset_index()

# grouped['Exporter'] = "Pacific"

# with open(f"{here}/pacific_mining_grouped.csv", 'w') as f:
#     grouped.to_csv(f, index=False, header=True)


# product_grouped = final.groupby(by=["Product"])['Value of the trade flow (thousands current USD)',
#        'Quantity (in metric tons)'].sum()

# product_grouped = product_grouped.reset_index()

# product_grouped['Exporter'] = "Pacific"

# with open(f"{here}/pacific_mining_product_grouped.csv", 'w') as f:
#     product_grouped.to_csv(f, index=False, header=True)


