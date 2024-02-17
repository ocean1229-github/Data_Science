import pandas as pd

df = pd.read_csv('data/world_cities.csv')

# 여기에 코드를 작성하세요
df['City / Urban area'].value_counts()
df['City / Urban area'].value_counts().shape

df['Country'].value_counts().shape

#df[]
df['pop'] = df['Population'] / df['Land area (in sqKm)']
new_df = df['pop'] > 10000
df[new_df].shape

#모범답안
df["Density"] = df["Population"] / df["Land area (in sqKm)"]
df_high_density = df[df["Density"] > 10000]
df_high_density.info()

density_ranks = df.sort_values(by="Density", ascending = False)
density_ranks['City / Urban area']