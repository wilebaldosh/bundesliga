import pandas as pd

df = pd.read_csv("data/raw/Bundesliga.csv")
print("df.head:")
print(df.head())

print("df.dtypes:")
print(df.dtypes)

print("df.info:")
print(df.info)

print("df.coluns:")
print(df.columns)

# Dos maneras diferentes de establecer los nombres de las columnas
# 1. Para todas las columnas
schema = ['index', 'homeTeam', 'awayTeam', 'homeGoals', 'awayGoals', 'round', 'year', 'date']
df.columns = schema
# 2. Sólo para las columnas seleccionadas
#df.rename(columns = {'Unnamed: 0': 'Index'}, inplace = True)
print("df.coluns:")
print(df.columns)

pd.to_datetime(df.date).dt.strftime("%Y-%M-%d $H:$M:$S")
print(df.head())
print("Count:")
print(df.count())

print("Filter by homeTeam and awayTeam that's contains: 'Freiburg'")
# freiburg = df[df['HomeTeam'].str.contains('Freiburg')]
freiburg = df.loc[df['homeTeam'].str.contains('Freiburg') | df['awayTeam'].str.contains('Freiburg')] 
print(freiburg.head())

print("Filter: homeGoals >= 10")
print(df.loc[df['homeGoals'] >= 10])

manyGoalsVector = df.loc[df['homeGoals'] >= 10]
print("manyGoalsVector: ")
print(manyGoalsVector)

# A DataFrame of a numerical type allows to use functions like min/max/mean.
# This allows to get things like:
print("Min year:")
print(df['year'].min())
print("Max date:")
print(df['year'].max())

print("Average home goals:")
print(df['homeGoals'].mean())

print("Average away oals:")
print(df['awayGoals'].mean())

maxDiff = abs(df['homeGoals'].max() - df['awayGoals'].max())
print("maxDiff:")
print(maxDiff)

print("Sort awayGoals: Descending")
print(df.sort_values(by = ['awayGoals'], ascending = False))

print("Check the total number of teams:")
print(len(df['homeTeam'].unique()))
print(df['homeTeam'].unique())
print()
print("unique from homeTeam and awayTeam")
print(pd.unique(df[['homeTeam', 'awayTeam']].values.ravel()))

# Let's find the most frequent results by using 'valueCounts'
print("Let's find the most frequent results by using 'valueCounts'")
print(pd.unique(df[['homeGoals', 'awayGoals']].values.ravel()))
print(pd.unique(df['homeGoals'].values.ravel()))
print(pd.unique(df['awayGoals'].values.ravel()))
frequent = df.set_index(['homeGoals', 'awayGoals']).count(level='awayGoals')
print("frequent:")
print(frequent)


merged_inner = pd.merge(left = df, right = df, left_on = 'index', right_on = 'index')
print("merged_inner.shape")
print(merged_inner.shape)
print("merged_inner")
print(merged_inner)
