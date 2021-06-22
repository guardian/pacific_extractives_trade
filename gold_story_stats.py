import pandas as pd 
import os
from paths import data_path 
from modules.yachtCharter import yachtCharter


# data_path = os.path.dirname(__file__)
# ceevee = f"{data_path}/data/baci_two_all_guardcat.csv"
ceevee = f"{data_path}/baci_three_all_guardcat.csv"

stats_path = os.path.dirname(__file__) + "/story_stats/"

df = pd.read_csv(ceevee)

# print(df)
# print(df.columns)


png_gold = df.loc[(df['hs4'] == 7108) & (df['Exporting country'] == 'Papua New Guinea')]

png_gold.loc[png_gold['Importing country'].isin(["India", "Italy", "Singapore"]), "Importing country"] = "Other"

grouped = png_gold.groupby(by=['Year', 'Exporting country', 'Importing country'])['Value of the trade flow (thousands current USD)',
       'Quantity (in metric tons)'].sum().reset_index()

grouped['What'] = "Gold"

with open(f"{stats_path}png_gold_exports.csv", "w") as f:
    grouped.to_csv(f, header=True, index=False)

# for_sankey = grouped[['Exporting country', 'Importing country',
# 'Quantity (in metric tons)']]

for_sankey = grouped[['Exporting country', 'Importing country',
'Value of the trade flow (thousands current USD)']]
for_sankey['Value of the trade flow (thousands current USD)'] = for_sankey['Value of the trade flow (thousands current USD)'] * 1000

for_sankey.columns = ["source", "target", "value"]



print(for_sankey)

def makeSankey(df):

    template = [
            {
                "title": "Papua New Guinea gold exports",
                "subtitle": f"Value of the gold exported in 2019 in US dollars",
                "footnote": "",
                "source": "CEPII's BACI trade dataset, Guardian analysis",
                # "dateFormat": "",
                # "yScaleType":"",
                # "xAxisLabel": "Days since first vaccination",
                # "yAxisLabel": "Doses per hundred people",
                # "minY": "",
                # "maxY": "",
                "periodDateFormat":"",
                "margin-left": "50",
                "margin-top": "15",
                "margin-bottom": "20",
                "margin-right": "20",
                "breaks":"no"
            }
        ]
    key = []
    periods = []
    labels = [{"x_pct":0, "y_pct":0, "text": "Exporters", "align":"start", "class":"heading"},
    {"x_pct":100, "y_pct":0, "text": "Importers", "align":"end", "class":"heading"}]
    chartId = [{"type":"sankey"}]
    df.fillna('', inplace=True)
    df = df.reset_index()
    chartData = df.to_dict('records')
    # print(since100.head())
    # print(chartData)
    yachtCharter(template=template, data=chartData, chartId=chartId,
     options=[], chartName="png_gold_export_sankey")
    
makeSankey(for_sankey)


