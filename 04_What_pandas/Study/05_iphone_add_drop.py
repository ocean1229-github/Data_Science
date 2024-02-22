import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv', index_col = 0)
iphone_df

# 요소추가
iphone_df.loc['iPhone XR'] = ['2018-10-26', 6.1, '3GB', 'iOS 12.0.1', 'Yes']

# 컬럼추가
iphone_df['제조사'] = 'Apple'

# 요소삭제
iphone_df.drop('iPhone XR', axis = 'index', inplace = True)
#inplace = False -> 기존 데이터 값을 고치지 않겠다. 시각적 용도로 사용하는 듯.
#inplace = True -> 완전한 삭제

#컬럼 지우기
iphone_df.drop('제조사', axis = 'columns', inplace = True)

# 여러개 지우기
iphone_df.drop(['iPhone 7', 'iPhone 8', 'iPhone X'], axis = 'index', inplace = True)