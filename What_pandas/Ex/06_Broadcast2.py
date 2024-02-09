import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
# 여기에 코드를 작성하세요
trueDF = df['KBS'] > 30
#df[trueDF] & df['KBS']

newDF = df[trueDF]

newDF['KBS']

# 모범답안 
import pandas as pd

df = pd.read_csv('data/broadcast.csv', index_col=0)
boolean_KBS = df['KBS'] > 30
df.loc[boolean_KBS, 'KBS']
