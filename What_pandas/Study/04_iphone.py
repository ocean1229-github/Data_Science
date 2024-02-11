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

#----------------------------------

iphone_df.loc[[True, False, True, True, False, True, False]]

iphone_df.loc[[True, False, False, True]]

iphone_df.loc[:, [True, False, False, True]]

iphone_df['디스플레이'] > 5

iphone_df.loc[iphone_df['디스플레이'] > 5]

iphone_df['Face ID'] == 'Yes'

iphone_df.loc[iphone_df['Face ID'] == 'Yes']

condition = (iphone_df['디스플레이'] > 5) & (iphone_df['Face ID'] == 'Yes'])
# | 이것도 가능

iphone_df(condition)

#-------------------------------------
#iloc
#loc -> location 
#iloc -> index location

iphone_df.iloc[2, 4]
# 'No'

iphone_df.iloc([1, 3], [1. 4])

iphone_df.iloc[3:, 1:4]


#--------------------------------------
iphone_df.loc['iPhone 8', '메모리']
iphone_df.loc['iPhone 8', '메모리'] = '2.5GB'
iphone_df.loc['iPhone 8', '출시버전'] = 'iOS 10.3'

iphone_df.loc['iPhone 8']

iphone_df.loc['iPhone 8'] = ['2016-09-22', '4.7', '2GB', 'iOS 11.0', 'No']

iphone_df['디스플레이']
iphone_df['디스플레이'] = ['4,7 in', '5,5 in', '4,7 in', '5,5 in', '5,8 in', '5,8 in', '6,5 in']

iphone_df['Face ID'] = 'No'


#---------------------------
iphone_df[['디스플레이', 'Face ID']]

iphone_df[['디스플레이', 'Face ID']] = 'x'
iphone_df

iphone_df.loc[['iPhone 7', 'iPhone X']]

iphone_df.loc[['iPhone 7', 'iPhone X']] = 'o'

iphone_df.loc['iPhone 7':'iPhone X']

#초기화
iphone_df['디스플레이'] > 5

iphone_df.loc[iphone_df['디스플레이'] > 5]

iphone_df.loc[iphone_df['디스플레이'] > 5] = 'p'

iphone_df.iloc[[1, 3], [1, 4]]

iphone_df.iloc[[1, 3], [1, 4]] = 'v'
