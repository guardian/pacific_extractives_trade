import pandas as pd 
import os 

here = os.path.dirname(__file__)
report_file = here + "/reports/"
sheets_file = here + "/balance_sheets/"
summaries_file = here + "/statistical_summaries/"
summary_csvs = here + "/summary_csvs/"

ceevee = f"{summary_csvs}1990summary.csv"

df = pd.read_csv(ceevee, header=None)
df.columns= ['unamed', 'None', '1990', '1989', '1988', '1987', '1986', '1985']

# df = df[['unamed', '1990', '1989', '1988', '1987', '1986', '1985']]

for year in ['1990', '1989', '1988', '1987', '1986', '1985']:
    df[year] = df[year].astype(str)
    df[year] = df[year].str.replace("B", '8')
    df[year] = df[year].str.replace('"', '')

    # df[year] = pd.to_numeric(df[year])

# df[['1990', '1989', '1988', '1987', '1986', '1985']] = df[['1990', '1989', '1988', '1987', '1986', '1985']].str.replace("B", '8')

print(df)

with open(f"{summary_csvs}1990summary.csv", "w") as f:
    df.to_csv(f, index=False, header=True)