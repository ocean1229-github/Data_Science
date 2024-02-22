import pandas as pd

world_cities = pd.read_csv('data/world_cities.csv')

# 여기에 코드를 작성하세요
world_cities['Country'].value_counts()

#모범답안
countries = world_cities['Country'].value_counts()
countries[countries == 4]
