import pandas as pd 
import os
from paths import data_path 
from modules.yachtCharter import yachtCharter


# data_path = os.path.dirname(__file__)
# ceevee = f"{data_path}/data/baci_two_all_guardcat.csv"
ceevee = f"{data_path}/baci_three_all_guardcat.csv"

stats_path = os.path.dirname(__file__) + "/story_stats/"

df = pd.read_csv(ceevee)

png = df.loc[df['Exporting country'] == 'Papua New Guinea'].copy()

png_minerals = png.loc[png['Category'] == "Oil, metals and mineral products"]

grouped = png_minerals.groupby(by=['Year', 'Exporting country', 'Importing country'])['Value of the trade flow (thousands current USD)',
       'Quantity (in metric tons)'].sum().reset_index()

with open(f"{stats_path}png_gold_exports.csv", "w") as f:
    grouped.to_csv(f, header=True, index=False)


grouped_totals = pd.DataFrame.from_records([{"Year": "2019", 
"Exporting country": "Papua New Guinea", 
"Importing country": "All",
"Value of the trade flow (thousands current USD)": grouped['Value of the trade flow (thousands current USD)'].sum(),
 "Quantity (in metric tons)": grouped['Quantity (in metric tons)'].sum()}])

total_grouped = grouped.append(grouped_totals)

print(total_grouped['Quantity (in metric tons)'].round())


for_sankey = grouped[['Exporting country', 'Importing country',
'Quantity (in metric tons)']].copy()

for_sankey.columns = ["source", "target", "value"]

for_sankey['Percentage of oz'] = (for_sankey['value']/616600.726)*100
# print()

for_sankey.loc[for_sankey['Percentage of oz'] < 30, 'target'] = "Other"

for_sankey = for_sankey.groupby(by=["source", "target"])["value"].sum().reset_index()

# print(for_sankey)

def makeSankey(df):

    template = [
            {
                "title": "Papua New Guinea mineral exports",
                "subtitle": f"Tonnes of minerals exported in 2019",
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
     options=[], chartName="png_mineral_export_sankey")
    
# makeSankey(for_sankey)