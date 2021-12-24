import pandas as pd
import re

df = pd.read_csv("pokemon_data.csv")

# read headers
df.columns

# read each column
df['Name']  # read a single row
df[["Name", "Type 1", "HP"]]  # read multiple rows

# reach each row
df.iloc(1)  # read row at index 1
df.iloc[0:4]  # reead rows o through 4
df[0:4]  # does the same thing
df.iloc[2, 1]  # read first column of the second item

# iterate through each row
for x, row in df.iterrows():
    # print(f'{x}:\n{row}\n')
    (str(x) + ":", row['Name'])

# filter by column
df.loc[df['Type 1'] == 'Fire']

# describe data with stats
df.describe()

# sort values by type 1 (acending) and hp (descending)
df.sort_values(['Type 1', 'HP'], ascending=[1, 0])

# add a column to existing dataframe
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + \
    df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# alternative (axis = 0 adds vertically, axis = 1 adds horizontally)
df['Total'] = df.iloc[:, 4:9].sum(axis=1)

# drop a column
df = df.drop(columns=['Total'])

# select columns by indexes
cols = list(df.columns.values)
df[cols[1:4] + [cols[-1]] + cols[4:12]]

df.to_excel('modified.xlsx', index=False)
df.to_csv('modifited.txt', sep='\t')

# filtering data
new_df = df.loc[('Type 1' == 'Grass') | (
    df['Type 2'] == 'Poison') & (df['HP'] > 70)]

# reset indexes and drop old indexes
new_df.reset_index(drop=True)

# get all names that contain mega
df.loc[df['Name'].str.contains('Mega')]

# get all names that don't contain mega
df.loc[~df['Name'].str.contains('Mega')]

# using regex
df.loc[~df['Type 1'].str.contains(
    'fire|grass', flags=re.I, regex=True)]
# all names that begin with 'pi'
df.loc[df['Name'].str.contains(
    '^pi[a-z]*', flags=re.I, regex=True)]

# conditional changes
# turn fire types to flamer
df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'

# make all fire types legendary
df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True

# modify multiple values
df.loc[df['HP'] > 50, ['Generation', 'Legenedary']] = ['Test 1', 'Test 2']

# reset
df = pd.read_csv("pokemon_data.csv")

# aggregate statistics (group by)
# get mean of all type 1s
df.groupby(['Type 1']).mean()

# order type 1 means
df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)

# sum
df.groupby(['Type 1']).sum()

# count
df['count'] = 1  # add count column
df.groupby(['Type 1']).count()['count']

# count subsets
df.groupby(['Type 1', 'Type 2']).count()['count']


new_df = pd.DataFrame(columns=df.columns)

# working with large amounts of data (iterate file through chunks of 5)
for df in pd.read_csv('pokemon_data.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results])  # compressed data

print(new_df)
