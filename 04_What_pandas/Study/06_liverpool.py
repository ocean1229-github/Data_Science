import pandas as pd

liverpool_df = pd.read_csv('data/liverpool.csv', index_col=0)
liverpool_df

#rename도 기존데이터에 간섭 x
liverpool_df.rename(columns={'position': 'Position'})

liverpool_df.rename(columns={'position': 'Position'}, inplace=True)

liverpool_df.rename(columns={'position': 'Position', 'born':'Born', 'number', 'Number', 'nationality': "Nationality"}, inplace=True)

liverpool_df.index.name = 'Player Name'
liverpool_df

# Number가 기준
liverpool_df.set_index('Number')

liverpool_df.index

liverpool_df['Player Name'] = liverpool_df.index
liverpool_df

# 얘도 기존에 간섭 x
liverpool_df.set_index('Number', inplace=True)