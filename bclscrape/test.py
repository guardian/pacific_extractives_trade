import pandas as pd 
import os 

here = os.path.dirname(__file__)
report_file = here + "/reports/"
sheets_file = here + "/balance_sheets/"
summaries_file = here + "/statistical_summaries/"
summary_csvs = here + "/summary_csvs/"

metrics = ['Ore and waste removed (millions of tonnes)', 'Total concentrate (thousands of dry tonnes)', 'Net earnings (loss)', 'Local employees']

listo = []

# for csv in os.listdir(summary_csvs):
#     path = f"{summary_csvs}{csv}"
#     df = pd.read_csv(path)
#     df.rename(columns={df.columns[0]: "Metric"}, inplace=True)
#     # df['Metric'] = df['Metric'].fillna(0)
#     df.loc[df['Metric'].str.contains('Ore and waste').fillna(False), 'Metric'] = 'Ore and waste removed (millions of tonnes)'
#     df.loc[df['Metric'].str.contains('Total concentrate').fillna(False), 'Metric'] = 'Total concentrate (thousands of dry tonnes)'
#     df.loc[df['Metric'].str.contains('Net earnings').fillna(False), 'Metric'] = 'Net earnings (loss)'
#     df.loc[df['Metric'].str.contains('National').fillna(False), 'Metric'] = 'Local employees'

#     df = df.loc[df['Metric'].isin(metrics)]
#     print(df)
#     listo.append(df)
# # 'Ore and waste'

#     # df = df.iloc[:, 0].str.contains('Ore and waste')
#     # print(df.loc[(df['Metric'].str.contains('Dividends').fillna(False)) | df['Metric'].str.contains('Dividends paid').fillna(False)])



df = pd.read_csv('/Users/josh_nicholas/github/pacific_extractives_trade/bclscrape/summary_csvs/2008summary.csv')


df["2007 2006"] = df["2007 2006"].fillna("0 0")
# df[['2007', '2006']] = df["2007 2006"].str.split(' ', expand=True)

df["2007 2006"] = df["2007 2006"].str.strip()

df['2007']= df["2007 2006"].str.split(' ', expand=True)[0]
df['2006']= df["2007 2006"].str.split(' ', expand=True)[1]

# print(df["2007 2006"].fillna("0 0"))
print(df)

### OLD CODE FOR RENAMING

# ceevee = f"{summary_csvs}1990summary.csv"

# df = pd.read_csv(ceevee, header=None)
# df.columns= ['unamed', 'None', '1990', '1989', '1988', '1987', '1986', '1985']

# # df = df[['unamed', '1990', '1989', '1988', '1987', '1986', '1985']]

# for year in ['1990', '1989', '1988', '1987', '1986', '1985']:
#     df[year] = df[year].astype(str)
#     df[year] = df[year].str.replace("B", '8')
#     df[year] = df[year].str.replace('"', '')

#     # df[year] = pd.to_numeric(df[year])

# # df[['1990', '1989', '1988', '1987', '1986', '1985']] = df[['1990', '1989', '1988', '1987', '1986', '1985']].str.replace("B", '8')

# print(df)

# with open(f"{summary_csvs}1990summary.csv", "w") as f:
#     df.to_csv(f, index=False, header=True)