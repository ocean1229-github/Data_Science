%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')

# Filter out rows where race_ethnicity is not equal to 'All'
mans = df[(df['job_category'] == 'Managers') & (df['gender'] == 'Male') & (df['race_ethnicity'] != 'All')]

mans.plot(kind='bar', x='race_ethnicity', y='count')


#모범답안
%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_summary.csv')
boolean_male = df['gender']=='Male'
boolean_manager = df['job_category'] == 'Managers'
boolean_not_all = df['race_ethnicity'] != 'All'

df[boolean_male & boolean_manager & boolean_not_all].plot(kind='bar', x='race_ethnicity',  y='count')
