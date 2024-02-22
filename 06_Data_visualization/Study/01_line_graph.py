%matplotlib inline

import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
df

df.plot(kind='line')

df.plot(y='KBS')

# 밑에 두 코드는 동일
df.plot(y=['KBS', 'JTBC'])

df[['KBS', 'JTBC']].plot()

# 밑에 두 코드는 동일
df['KBS']

df['KBS'].plot()

# 숫자만 그래프로 가능 문자의 경우 선 그래프 불가능 