import pandas as pd 
import os
from paths import data_path 

ceevee = f"{data_path}/baci_three_all_guardcat.csv"

extract = os.path.dirname(__file__) + "/extracts/"


def sankey_output(frame, measure, minimum, countries, extractives_or_no, measure_name):

    if extractives_or_no == 0:
        df = frame

        print("#### Total exports \n\n")

    else: 
        df = frame.loc[frame['Category'] != "Other"]

        print("#### Extractive exports \n\n")

    # just exporting countries we want

    df = df.loc[df['Exporting country'].isin(countries)]

    # eliminate recursion

    pac_df = df.loc[~df['Importing country'].isin(countries)]

    grouped = pac_df.groupby(['Exporting country', 'Importing country'])[measure].sum().reset_index()

    grouped[measure] = grouped[measure].round()

    ### figure out who the little importers are so they can be renamed

    importers = df.groupby(['Importing country'])[measure].sum().reset_index()

    importers[measure] = pd.to_numeric(importers[measure])

    lil_importers = importers.loc[importers[measure] <= minimum]

    lil_importers = lil_importers['Importing country'].values.tolist()

    ### rename little importers

    grouped.loc[grouped['Importing country'].isin(lil_importers), 'Importing country'] = 'Other'

    grouped = grouped.groupby(['Exporting country', 'Importing country'])[measure].sum().reset_index()

    # with open(f"{data_path}/data/sankey_output_{measure_name}.csv", "w") as f:
    #     grouped.to_csv(f, index=False, header=True)

    return grouped

### SETUP    

df = pd.read_csv(ceevee)

# print(df)

pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

# exporters = ['Papua New Guinea', "Solomon Isds", "Malaysia"]


# which_measure = "Quantity (in metric tons)"



#### GET PACIFIC EXTRACTIVE EXPORTS

# pacific_extractive = sankey_output(df, which_measure, 100, pacific, 1, "weight")

# df = pacific_extractive


####

# df = df.loc[df['Category'] == 'Wood products']

# grouped = sankey_output(df, which_measure, 100000, pacific, 1, "weight")



# ### JUST MINERAL EXPORTS

# which_measure = 'Quantity (in metric tons)'

# df = df.loc[df['Category'] == "Oil, metals and mineral products"]

# grouped = sankey_output(df, which_measure, 100000, pacific, 1, "weight")

which_measure = 'Value of the trade flow (thousands current USD)'

df = df.loc[df['Category'] == "Oil, metals and mineral products"]

grouped = sankey_output(df, which_measure, 100000, pacific, 1, "dollar")

exporters = grouped.groupby(['Exporting country'])[which_measure].sum().reset_index()

### EXCLUDE EXPORTERS WHO EXPORT LESS THAN 1K TONNES

lil_exporters = exporters.loc[exporters[which_measure] <= 1000]

lil_exporters = lil_exporters['Exporting country'].values.tolist()

grouped = grouped.loc[~grouped['Exporting country'].isin(lil_exporters)]

print(grouped)

with open(f"{extract}mineralexporters_sankey_output_{which_measure}.csv", "w") as f:
    grouped.to_csv(f, index=False, header=True)

# print(grouped)

### JUST THE WOOD EXPORTERS

# df = df.loc[df['Category'] == 'Wood products']

# grouped = sankey_output(df, which_measure, 100000, exporters, 1, "weight")

# print(grouped)

# with open(f"{data_path}/data/woodexporters_sankey_output_{which_measure}.csv", "w") as f:
#     grouped.to_csv(f, index=False, header=True)


### GROUP ALL OF PACIFIC TOGETHER

# which_measure = 'Quantity (in metric tons)'

# grouped = sankey_output(df, which_measure, 100000, pacific, 1, "tonnes")

# # which_measure = 'Value of the trade flow (thousands current USD)'

# # grouped = sankey_output(df, which_measure, 100000, pacific, 1, "dollars")

# grouped['Exporting country'] = 'Pacific'

# grouped = grouped.groupby(['Exporting country', 'Importing country'])[which_measure].sum().reset_index()

# grouped[which_measure] = pd.to_numeric(grouped[which_measure])
# grouped = grouped.sort_values(by=which_measure, ascending=False)

# print(grouped.sort_values(which_measure, ascending=False))

# with open(f"{extract}pacific_grouped_sankey_output_{which_measure}.csv", "w") as f:
#     grouped.to_csv(f, index=False, header=True)

# ### MAKE A PYTHON SANKEY



# import holoviews as hv 


# hv.extension('bokeh')
# from bokeh.plotting import show

# figfig = hv.Sankey(grouped, kdims=['Exporting country', 'Importing country'], vdims=[which_measure])

# figfig.opts(cmap='Colorblind',label_position='left',
#                                  edge_color='Importing country', edge_line_width=0,
#                                  node_alpha=1, node_width=40, node_padding=10, node_sort=True,
#                                  width=800, height=1000, bgcolor="snow",
#                                  title="Pacific exports of mineral products by weight")


# show(hv.render(figfig))




