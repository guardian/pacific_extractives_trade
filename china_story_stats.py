import pandas as pd 
import os
from paths import data_path 
from modules.yachtCharter import yachtCharter


# data_path = os.path.dirname(__file__)
# ceevee = f"{data_path}/data/baci_two_all_guardcat.csv"
ceevee = f"{data_path}/baci_three_all_guardcat.csv"

stats_path = os.path.dirname(__file__) + "/story_stats/"

df = pd.read_csv(ceevee)
pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

### CUT DOWN TO ONLY PACIFIC COUNTRIES AS EXPORTERS

pac_df = df.loc[df['Exporting country'].isin(pacific)]
extrac_df = pac_df.loc[pac_df['Category'] != "Other"]

china = pac_df.loc[pac_df['Importing country']== "China"]

# print(china)

# china_cat = china.groupby(by=["Year",'Importing country', 'Category'])['Value of the trade flow (thousands current USD)', 'Quantity (in metric tons)'].sum().reset_index()
china_cat = china.groupby(by=["Year",'Importing country', 'Category'])['Quantity (in metric tons)'].sum().reset_index()

print(china_cat.round())
# pacific = ['Papua New Guinea',"Fiji",'Solomon Isds',"Vanuatu","Samoa","Tonga","Cook Isds","Tuvalu","Niue", "FS Micronesia","Kiribati","Marshall Isds","Palau","Nauru"]

# pac = df.loc[df['Exporting country'].isin(pacific)]

# grouped = pac.groupby(by=['Year', 'Exporting country', 'Importing country'])['Value of the trade flow (thousands current USD)',
#        'Quantity (in metric tons)'].sum().reset_index()

# with open(f"{stats_path}png_gold_exports.csv", "w") as f:
#     grouped.to_csv(f, header=True, index=False)

# for_sankey = grouped[['Exporting country', 'Importing country',
# 'Quantity (in metric tons)']]

# for_sankey.columns = ["source", "target", "value"]

# for_sankey['Percentage of oz'] = (for_sankey['value']/616600.726)*100
# # print()

# for_sankey.loc[for_sankey['Percentage of oz'] < 30, 'target'] = "Other"

# for_sankey = for_sankey.groupby(by=["source", "target"])["value"].sum().reset_index()

# print(for_sankey)

# def makeSankey(df):

#     template = [
#             {
#                 "title": "Papua New Guinea mineral exports",
#                 "subtitle": f"Tonnes of minerals exported in 2019",
#                 "footnote": "",
#                 "source": "CEPII's BACI trade dataset, Guardian analysis",
#                 # "dateFormat": "",
#                 # "yScaleType":"",
#                 # "xAxisLabel": "Days since first vaccination",
#                 # "yAxisLabel": "Doses per hundred people",
#                 # "minY": "",
#                 # "maxY": "",
#                 "periodDateFormat":"",
#                 "margin-left": "50",
#                 "margin-top": "15",
#                 "margin-bottom": "20",
#                 "margin-right": "20",
#                 "breaks":"no"
#             }
#         ]
#     key = []
#     periods = []
#     labels = [{"x_pct":0, "y_pct":0, "text": "Exporters", "align":"start", "class":"heading"},
#     {"x_pct":100, "y_pct":0, "text": "Importers", "align":"end", "class":"heading"}]
#     chartId = [{"type":"sankey"}]
#     df.fillna('', inplace=True)
#     df = df.reset_index()
#     chartData = df.to_dict('records')
#     # print(since100.head())
#     # print(chartData)
#     yachtCharter(template=template, data=chartData, chartId=chartId,
#      options=[], chartName="png_mineral_export_sankey")
    
# makeSankey(for_sankey)