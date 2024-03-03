%matplotlib inline

import pandas as pd
df = pd.read_csv('data/world_indexes.csv')

df.plot(kind='scatter', x='Life expectancy at birth- years', y= 'Internet users percentage of population 2014')
df.plot(kind='scatter', x='Forest area percentage of total land area 2012', y= 'Carbon dioxide emissionsAverage annual growth')
df.plot(kind='scatter', x='Internet users percentage of population 2014', y= 'Forest area percentage of total land area 2012')
df.plot(kind='scatter', x='Life expectancy at birth- years', y= 'Carbon dioxide emissionsAverage annual growth')
df.plot(kind='scatter', x='Life expectancy at birth- years', y='Forest area percentage of total land area 2012')