import pandas as pd

iphone_df = pd.read_csv('iphone.csv', index_col = 0)
iphone_df

iphone_df.loc['iPhone 8', '메모리']

iphone_df.loc['iPhone X', :]
# 전체 데이터 가져옴

iphone_df.loc['iPhone X']
#위 코드랑 같음
#타입은 시리즈

type(iphone_df.loc['iPhone X'])

iphone_df.loc[:, '출시일']