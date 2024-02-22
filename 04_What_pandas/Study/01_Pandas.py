import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns = ['name', 'english_score', 'math_score'], index = ['a', 'b', 'c', 'd'])
my_df

type(my_df)

my_df.columns

my_df.index

my_df