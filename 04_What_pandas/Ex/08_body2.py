import pandas as pd

df = pd.read_csv('data/body_imperial2.csv', index_col=0)

# 여기에 코드를 작성하세요
df['비만도'] = '정상'
df.loc[df.index <= 10, 'Gender'] = 'Male'
df.loc[df.index > 10, 'Gender'] = 'Female'

# 테스트 코드
df

#모범 답안
df["비만도"] = "정상"
df.loc[:10,"Gender"] = "Male"
df.loc[11:,"Gender"] = "Female"