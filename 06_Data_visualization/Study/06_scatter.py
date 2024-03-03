#산점도
%matplotlib inline

import pandas as pandas
df = pd.read_csv('data/exam.csv')
df.head()

df.plot(kind='scatter', x='math score', y='reading score')

df.plot(kind='scatter', x='math score', y='writing score')

df.plot(kind='scatter', x='reading score', y='writing score')