import tabula 
import os 


here = os.path.dirname(__file__)
report_file = here + "/reports/"
sheets_file = here + "/balance_sheets/"
summaries_file = here + "/statistical_summaries/"
summary_csvs = here + "/summary_csvs/"

eightyone = f'{summaries_file}summaries_1981.pdf'

# df = tabula.read_pdf(eightyone)[0]

# df = df[['Unnamed: 2', '1981 1980', '1979 1978',
#        '1977', '1976', 'Unnamed: 3', '1975', '1974 1973',
#        '1972"']]

# with open(f"{summary_csvs}1981summary.csv", "w") as f:
#     df.to_csv(f, index=False, header=True)

eightyfive = f'{summaries_file}summaries_1985.pdf'

# df = tabula.read_pdf(eightyfive)[0]

# with open(f"{summary_csvs}1985summary.csv", "w") as f:
#     df.to_csv(f, index=False, header=True)

ninety = f'{summaries_file}summaries_1990.pdf'

# df = tabula.read_pdf(ninety, pages="2")[0]
# print(df)
# print(df.columns)

# with open(f"{summary_csvs}1990summary.csv", "w") as f:
#     df.to_csv(f, index=False, header=True)

oheight = f'{summaries_file}summaries_2008.pdf'

df = tabula.read_pdf(oheight, pages="2")[0]
df.columns = df.loc[1]
df = df[2:]

with open(f"{summary_csvs}2008summary.csv", "w") as f:
    df.to_csv(f, index=False, header=True)

# dfs = tabula.read_pdf(testo, pages='2')

# dfs = tabula.read_pdf(testo, pages=['0', '1'])
# print(dfs[0])

# print(dfs)

# print(dfs[0].columns)

# print(dfs)

# df[['1981', '1980']] = df['1981 1980'].str.split(" ", expand=True)
# # df[['1979', '1978']] = df['1981 1980'].str.split(" ", expand=True)

# print(df)