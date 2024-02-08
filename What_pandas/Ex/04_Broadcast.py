import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)

# 여기에 코드를 작성하세요
df.loc[2016, 'KBS']

df.loc[:,'JTBC']
# 왜 df['JTBC']는 되는데 .loc을 붙이면 안되는지

df.loc[:, ('SBS', 'JTBC')]