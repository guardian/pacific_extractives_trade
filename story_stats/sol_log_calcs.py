import pandas as pd 
import os
from paths import data_path

ceevee = f"{data_path}/pac_baci_three_all_guardcat_hs6.csv"
extract = os.path.dirname(__file__) + "/extracts/"

# hs6_codes = 

df = pd.read_csv(ceevee)

codes = f"{data_path}/product_codes_HS17_V202102.csv"

codes = pd.read_csv(codes)

merged = pd.merge(df, codes, left_on="Product category", right_on="code", how="left")

sol = merged.loc[merged['Exporting country'] == 'Solomon Isds'].copy()


sol_wood = sol.loc[sol['Category'] == "Wood products"]



## WORK OUT TOTALS FOR PIECE

print(f"Total logs exported: {sol_wood['Quantity (in metric tons)'].sum()}")


totals = sol.groupby(by="Category")['Quantity (in metric tons)'].sum().reset_index()

total_tonnes = totals['Quantity (in metric tons)'].sum()

totals['Percent'] = (totals['Quantity (in metric tons)']/total_tonnes)*100


print(totals)

# print(totals)

# print(df)

# pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

# pacific = df.loc[df['Exporting country'].isin(pacific)]


# with open(f"{data_path}/pac_baci_three_all_guardcat_hs6.csv", 'w') as f:
#     pacific.to_csv(f, index=False, header=True)
