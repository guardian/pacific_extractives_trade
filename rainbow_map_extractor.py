import pandas as pd
import os
from paths import data_path

pd.options.display.float_format = '{:.0f}'.format

ceevee = f"{data_path}/baci_three_all_guardcat.csv"
extract = os.path.dirname(__file__) + "/extracts/"

df = pd.read_csv(ceevee)


def sankey_output(frame, measure, minimum, countries, extractives_or_no):

    if extractives_or_no == 0:
        df = frame

        print("#### Total exports \n\n")

    else:
        df = frame.loc[frame['Category'] != "Other"]

        print("#### Extractive exports \n\n")

    # just exporting countries we want

    pac_df = df.loc[df['Exporting country'].isin(countries)]

    # eliminate recursion

    pac_df = pac_df.loc[~df['Importing country'].isin(countries)]


    ### MAKE REAL NUMBERS

    # pac_df[measure] = pac_df[measure] * 1000


    grouped = pac_df.groupby(['Exporting country', 'Importing country', "Category"])[measure].sum().reset_index()

    grouped[measure] = grouped[measure].round()

    ### figure out who the little importers are so they can be renamed

    importers = df.groupby(['Importing country'])[measure].sum().reset_index()

    importers[measure] = pd.to_numeric(importers[measure])

    lil_importers = importers.loc[importers[measure] <= minimum]

    lil_importers = lil_importers['Importing country'].values.tolist()

    ### rename little importers

    grouped.loc[grouped['Importing country'].isin(lil_importers), 'Importing country'] = 'Other'

    grouped = grouped.groupby(['Exporting country', 'Importing country', "Category"])[measure].sum().reset_index()

    # with open(f"{data_path}/data/sankey_output_{measure_name}.csv", "w") as f:
    #     grouped.to_csv(f, index=False, header=True)

    return grouped

### SETUP

df = pd.read_csv(ceevee)

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

# pacific = ['Papua New Guinea',"Fiji",'Solomon Isds']
# exporters = ['Papua New Guinea', "Solomon Isds", "Malaysia"]

df = pd.read_csv(ceevee)

# print(df)

which_measure = "Quantity (in metric tons)"
# which_measure = 'Value of the trade flow (thousands current USD)'

#### GET PACIFIC EXTRACTIVE EXPORTS

pacific_extractive = sankey_output(df, which_measure, 100, pacific, 1)

df = pacific_extractive

#### RENAME COUNTRIES FOR CENTROIDS


df.loc[df['Exporting country'] == "FS Micronesia", 'Exporting country'] = "Federated States of Micronesia"
df.loc[df['Importing country'] == "FS Micronesia", 'Importing country'] = "Federated States of Micronesia"

df.loc[df['Exporting country'] == "Cook Isds", 'Exporting country'] = "Cook Islands"
df.loc[df['Importing country'] == "Cook Isds", 'Importing country'] = "Cook Islands"

df.loc[df['Exporting country'] == "Solomon Isds", 'Exporting country'] = "Solomon Islands"
df.loc[df['Importing country'] == "Solomon Isds", 'Importing country'] = "Solomon Islands"

df.loc[df['Exporting country'] == "Marshall Isds", 'Exporting country'] = "Marshall Islands"
df.loc[df['Importing country'] == "Marshall Isds", 'Importing country'] = "Marshall Islands"

df.loc[df['Importing country'] == "United Rep. of Tanzania", 'Importing country'] = "Tanzania"

df.loc[df['Importing country'] == "Rep. of Korea", 'Importing country'] = "Republic of Korea"
df.loc[df['Importing country'] == "Viet Nam", 'Importing country'] = "Vietnam"
df.loc[df['Importing country'] ==  "USA", 'Importing country'] = "United States"
df.loc[df['Importing country'] ==  "France, Monaco", 'Importing country'] = "France"

df.loc[df['Importing country'] ==  "Dem. People's Rep. of Korea", 'Importing country'] = "Dem. Rep. Korea"

df.loc[df['Importing country'] ==  "Belgium-Luxembourg", 'Importing country'] = "Belgium"
df.loc[df['Importing country'] ==  "Switzerland, Liechtenstein", 'Importing country'] = "Switzerland"
df.loc[df['Importing country'] == "Norway, Svalbard and Jan Mayen", 'Importing country'] = "Norway"

df.loc[df['Importing country'] ==  "China, Macao Special Administrative Region", 'Importing country'] = "China"
# df.loc[df['Importing country'] ==  "China, Macao SAR", 'Importing country'] = "China"


df.loc[df['Importing country'] ==  "So. African Customs Union", 'Importing country'] = "South Africa"
df.loc[df['Importing country'] ==  "Czechia", 'Importing country'] = "Czech Republic"

df.loc[df['Importing country'] ==  "Norfolk Islands", 'Importing country'] = "Norfolk Island"
df.loc[df['Importing country'] == "United Republic of Tanzania", 'Importing country'] = "Tanzania"
df.loc[df['Importing country'] ==  "Lao People's Dem. Rep.", 'Importing country'] = "Lao PDR"
df.loc[df['Importing country'] ==  "The Former Yugoslav Republic of Macedonia", 'Importing country'] = "Macedonia"
df.loc[df['Importing country'] ==  "China, Hong Kong SAR", 'Importing country'] = "Hong Kong"

df.loc[df['Importing country'] ==  "C�te d'Ivoire", 'Importing country'] = "CÃ´te d'Ivoire"
df.loc[df['Importing country'] ==  "C√¥te d'Ivoire", 'Importing country'] = "CÃ´te d'Ivoire"

df.loc[df['Importing country'] ==  "Dem. Rep. of the Congo", 'Importing country'] = "Democratic Republic of the Congo"

df.loc[df['Importing country'] ==  "Dominican Rep.", 'Importing country'] = "Dominican Republic"


exclude = ["North Macedonia", "Bosnia Herzegovina", "Bolivia (Plurinational State of)", "Wallis and Futuna Isds", "Norfolk Isds", "Curaçao", "Christmas Isds", "Cocos Islands", "Other Asia, not elsewhere specified", "Other Asia, nes", "Cura�ao", "Christmas Islands"]

df = df.loc[~df['Exporting country'].isin(exclude)]
df = df.loc[~df['Importing country'].isin(exclude)]


### MAKE IT A WIDE FORMAT

pivoted = df.pivot(index=["Exporting country", "Importing country"], columns = "Category", values=which_measure).reset_index()

pivoted = pivoted.fillna(0)

if which_measure == 'Value of the trade flow (thousands current USD)':
    pivoted[["Oil, metals and mineral products", "Seafood products", "Wood products"]] = pivoted[["Oil, metals and mineral products", "Seafood products", "Wood products"]] * 1000

# print(pivoted)

# print(pivoted['Exporting country'].unique())

# with open(f"{data_path}/data/pac_rainbow_exports.csv", "w") as f:
#     pivoted.to_csv(f, index=False, header=True)

# with open('/Users/josh_nicholas/PTP_final_clean/charts/pac_rainbow/assets/pac_rainbow_exports.csv', "w") as f:
#     pivoted.to_csv(f, index=False, header=True)

#### CREATE A COMBINED PACIFIC EXPORT DATASET

pacific_grouped = pivoted.groupby(['Importing country'])['Oil, metals and mineral products', 'Seafood products',
       'Wood products'].sum().reset_index()

pacific_grouped['Exporting country'] = 'Total Pacific'



# print(pacific_grouped)

combined = pivoted.append(pacific_grouped)

# print(combined['Exporting country'].unique())

# print(combined)

if which_measure == 'Value of the trade flow (thousands current USD)':
    which_measure = 'Value of the trade flow (current USD)'


with open(f"{extract}pac_indi_grouped_rain_{which_measure}.csv", "w") as f:
    combined.to_csv(f, index=False, header=True)


print("\n\n\n\n\n")
print(combined)
# python3 /Users/josh_nicholas/PTP_final_clean/baci_clean/rainbow_map_extractor.py

# tuvastraya = combined.loc[(combined['Exporting country'] == "Tuvalu") & (combined['Importing country'] == "Singapore") ]

# print(tuvastraya)

# print(combined.loc[combined['Exporting country'] == "Tuvalu"])
