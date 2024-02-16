import pandas as pd

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