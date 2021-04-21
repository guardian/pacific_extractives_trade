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

pac_df = df.loc[df['Exporting country'].isin(pacific)]



def china_pct(frame, pac_frame, metric, extratives_or_no):

    ### THIS FUNCTION IS TO FIGURE OUT WHAT PERCENTAGE OF TOTAL EXPORTS GO TO CHINA - FOR THE WORLD AND PACIFIC REGION, ALL EXPORTS OR EXTRACTIVES (BOOLEAN)

    print(f"Looking up {metric}")

    ### Cut down frame to only be extractives, or not

    if extratives_or_no == 0:
        frame = frame

        print("#### Total exports \n\n")

    else: 
        frame = frame.loc[frame['Category'] != "Other"]

        print("#### Extractive exports \n\n")


    ### Work out world totals

    total_exports = frame[metric].sum()
    china_imports = frame.loc[frame['Importing country'] == 'China'][metric].sum()
    
    china_pct_world_exports = (china_imports / total_exports) * 100

    ### Work out Pacific totals

    pac_df = pac_frame

    total_pac_exports = pac_df[metric].sum()
    china_pac_imports = pac_df.loc[pac_df['Importing country'] == 'China'][metric].sum()

    china_pct_pac_exports = (china_pac_imports / total_pac_exports) * 100

    return {
        "China World percentage": {china_pct_world_exports}, 
        "China Pac percentage": {china_pct_pac_exports}
    }


# total = china_pct(df, pac_df, which, 0)
# extractives = china_pct(df, pac_df, which, 1)

# print(total)
# print(extractives)

def rest_of_pacific(pac_frame, metric, extratives_or_no):

    #### FUNCTION FIGURE OUT CHINA'S SHARE OF EACH COUNTRY'S EXPORTS, ALL EXPORTS OR EXTRACTIVES (BOOLEAN)

    if extratives_or_no == 0:
        pac_frame = pac_frame

        print("#### Total exports \n\n")

    else: 
        pac_frame = pac_frame.loc[pac_frame['Category'] != "Other"]

        print("#### Extractive exports \n\n")



    pac_grouped = pac_frame.groupby(['Exporting country', 'Importing country'])[which].sum().reset_index()

    # work out total exported per country

    pac_total = pac_grouped.groupby(['Exporting country'])[which].sum().reset_index()

    # work out total exported to China per country

    pac_china = pac_grouped.loc[pac_grouped['Importing country'] == 'China']

    pac_china_total = pac_china.groupby(['Exporting country'])[which].sum().reset_index()

    # combine the two datasets and clean up

    pac_total.rename(columns = {"Quantity (in metric tons)":"Tonnes exported" }, inplace=True)

    pac_china.rename(columns = {"Quantity (in metric tons)":"Tonnes exported to China" }, inplace=True)

    pac_final = pac_total.merge(pac_china, on="Exporting country")

    pac_final.drop(columns=['Importing country'], inplace=True)

    # if which == 

    pac_final['Percent exported to China'] = (pac_final['Tonnes exported to China'] / pac_final['Tonnes exported']) * 100

    return pac_final.round()




print("Figuring out extractive exports\n\n")

# world_extractives = china_pct(df, pac_df, which, 1)
pac_df = pac_df.loc[pac_df['Category'] == 'Oil, metals and mineral products']
pac_extractives = rest_of_pacific(pac_df, which, 1)

# print(world_extractives)
print(pac_extractives)