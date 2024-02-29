%matplotlib inline
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')

# 여기에 코드를 작성하세요
adobe_df = (df['count'] > 0) & (df['company'] == 'Adobe') & (df['race'] == 'Overall_totals')
except_df = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')

df[adobe_df & except_df].set_index('job_category').plot(kind='pie', y= 'count')

#모범답안
%matplotlib inline
import pandas as pd

df = pd.read_csv("data/silicon_valley_details.csv")

boolean_adobe = df['company'] == 'Adobe'
boolean_all_races = df['race'] == 'Overall_totals'
boolean_count = df['count'] != 0
boolean_job_category = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')

df_adobe = df[boolean_adobe & boolean_all_races & boolean_count & boolean_job_category]
df_adobe.set_index('job_category', inplace=True)
df_adobe.plot(kind='pie', y= 'count')
