# import chord
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt 

import pandas as pd 
import os
from paths import data_path

ceevee = f"{data_path}/baci_three_all_guardcat.csv"
extract = os.path.dirname(__file__) + "/extracts/"


df = pd.read_csv(ceevee)

exporters = ['Papua New Guinea', "Solomon Isds", "Malaysia"]

df = pd.read_csv(ceevee)


### EXTRACTIVES OR EVERYTHING - exclude "Other" in the category to make it only extractives

# df = df.loc[df['Category'] != "Other"]


three_df = df.loc[df['Exporting country'].isin(exporters)]

three_wood_df = three_df.loc[three_df['Category'] == "Wood products"]

three_grouped = three_wood_df.groupby(['Exporting country', 'Importing country'])["Quantity (in metric tons)"].sum().reset_index()

three_grouped = three_grouped.sort_values(by="Quantity (in metric tons)", ascending=False)


#### create a group with only smaller importers


lil_importers = three_grouped.loc[three_grouped["Quantity (in metric tons)"] <= 1000]

lil_importers = lil_importers['Importing country'].values.tolist()


### rename little importers to "other"

three_grouped.loc[three_grouped['Importing country'].isin(lil_importers), 'Importing country'] = 'Other'

three_grouped = three_grouped.groupby(['Exporting country', 'Importing country'])["Quantity (in metric tons)"].sum().reset_index()

three_grouped["Quantity (in metric tons)"] = pd.to_numeric(three_grouped["Quantity (in metric tons)"])
three_grouped = three_grouped.sort_values(by="Quantity (in metric tons)", ascending=False)

with open(f"{extract}malaysia_png_sols_log_sankey_tonnes.csv", "w") as f:
    three_grouped.to_csv(f, index=False, header=True)

print(three_grouped)
### MAKE A PYTHON SANKEY

# import holoviews as hv 


# hv.extension('bokeh')
# from bokeh.plotting import show

# figfig = hv.Sankey(three_grouped, kdims=['Exporting country', 'Importing country'], vdims=["Quantity (in metric tons)"])

# figfig.opts(cmap='Colorblind',label_position='left',
#                                  edge_color='Importing country', edge_line_width=0,
#                                  node_alpha=1, node_width=40, node_padding=10, node_sort=True,
#                                  width=800, height=1000, bgcolor="snow",
#                                  title="Tonnes of wood exports from Solomon Islands, PNG and Malaysia")


# show(hv.render(figfig))
