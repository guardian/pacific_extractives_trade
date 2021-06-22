import pandas as pd
from modules.yachtCharter import yachtCharter
import os

here = os.path.dirname(__file__)
data_path = os.path.dirname(__file__) + "/data/"
output_path = os.path.dirname(__file__) + "/output/"

fillo = f"{data_path}"

ceevee = f'{here}/stbarbara.xlsx'

df = pd.read_excel(ceevee)
# df = df.pivot(index=)
df = df.T
df.columns = ["Simberi Operations revenue",
  "Simberi Operations gross profit",
    "Simberi Operations royalties paid",
      "St Barbara income tax paid in PNG"]

df = df[1:]
print(df)
print(df.columns)


# python3 /Users/josh_nicholas/github/pacific_extractives_trade/taxes/stbar_groupedbar.py
def makeGroupedBar(df):

    template = [
            {
                "title": "Revenues, gross profit and taxes paid in PNG by St Barbara",
                "subtitle": "Measured in Australian dollars, taxes paid include income taxes, royalties, wage/salary taxes, and other taxes/duties",
                "footnote": "",
                "source": " | St Barbara annual and sustainability reports; St Barbara response to Guardian Australia questions",
                # "dateFormat": "",
                # "yScaleType":"",
                # "xAxisLabel": "",
                # "yAxisLabel": "",
                # "minY": "",
                # "maxY": "",
                # "periodDateFormat":"",
                "tooltip": "True",
                "margin-left": "50",
                "margin-top": "15",
                "margin-bottom": "20",
                "margin-right": "10",
                # "breaks":"no"
            }
        ]
    key = [{"key":"Simberi Operations revenue","colour":"#fb8072"},
{"key":"Simberi Operations gross profit","colour":"#999999"},
{"key":"Simberi Operations royalties paid","colour":"#67a9cf"},
{"key":"St Barbara income tax paid in PNG","colour":"#00bfff"}]
    periods = []
    labels = []
    # chartId = [{"type":"linechart"}]
    df.fillna('', inplace=True)
    df = df.reset_index()
    chartData = df.to_dict('records')
    # print(since100.head())

    yachtCharter(template=template, data=chartData, chartId=[{"type":"groupedbar"}], key=key, options=[{"enableShowMore":0}], chartName="st-barbara-revenue-taxes")

makeGroupedBar(df)
