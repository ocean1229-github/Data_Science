import pandas as pd

laptops_df = pd.read_csv('data/laptops.csv')

laptops_df.head(3)
laptops_df.head(7)
laptops_df.tail(6)
laptops_df.shape
# (167, 15) # 167개의 로우와 15개의 컬럼

laptops_df.columns

laptops_df.info()
laptops_df.describe()
# 통계값들이 나옴

laptops_df.sort_values(by='price')
#가격 순으로 나열

laptops_df.sort_values(by='price', ascending=False, inplace=True)
# 기존 그래프 터

laptops_df

laptops_df['brand']

laptops_df['brand'].unique()
# 명칭이 겹치지 않는 유니크한 명칭만

laptops_df['brand'].value_counts()
# 각 브랜드 별 개수

laptops_df['brand'].describe()
# 전체 값 통계(요약본)