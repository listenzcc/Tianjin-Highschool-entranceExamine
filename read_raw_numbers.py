"""
File: read_raw_numbers.py
Author: Chuncheng Zhang
Date: 2023-07-08
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-07-08 ------------------------
# Requirements and constants
import pandas as pd
import plotly.express as px

from rich import print
from pathlib import Path
from tqdm.auto import tqdm


# %% ---- 2023-07-08 ------------------------
# Function and class
df = pd.read_excel(Path('raw-numbers.xlsx'))
df


# %% ---- 2023-07-08 ------------------------
# Play ground
data = []

for col in tqdm(df.columns):
    lst = df[col].dropna().to_list()
    m = len([e for e in lst if str(e).endswith('以上')])
    n = len(lst)
    print(col.strip(), n, m)
    for j in range(m):
        data.append((lst[j], lst[j+m], lst[j+m*2]))

table = pd.DataFrame(data, columns=['Segment', 'nTotal', 'nUrban'])
table['Segment'] = table['Segment'].map(lambda e: int(e[:3]))
table['nSuburb'] = table['nTotal'] - table['nUrban']


for pos in ['Total', 'Urban', 'Suburb']:
    table['d'+pos] = 0
    table['sum' + pos] = table['n' + pos].max()
    for idx in table.index[1:]:
        table.loc[idx, 'd'+pos] = table.loc[idx,
                                            'n'+pos] - table.loc[idx-1, 'n'+pos]

    table['ratio'+pos] = table['n'+pos] / table['n'+pos].max()

table['Year'] = '2023'
table.to_csv('numbers.csv')
print(table)


# %% ---- 2023-07-08 ------------------------
# Pending
fig = px.scatter(table, x='Segment', y=['dTotal', 'dUrban', 'dSuburb'])
fig.update_xaxes(autorange="reversed")
fig.show()

fig = px.scatter(table, x='Segment', y=['nTotal', 'nUrban', 'nSuburb'])
fig.update_xaxes(autorange="reversed")
fig.show()

fig = px.scatter(table, x='Segment', y=[
                 'ratioTotal', 'ratioUrban', 'ratioSuburb'])
fig.update_xaxes(autorange="reversed")
fig.show()

# %% ---- 2023-07-08 ------------------------
# Pending


# %%
