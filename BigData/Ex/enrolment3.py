import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 여기에 코드를 작성하세요

# 조건 1


# 조건 2
not_assigned = df['status'] == 'not allowed'
df.loc[not_assigned, 'room assignment'] = 'not assigned'

# 조건 3
df.rename(columns = {'room assignment' : 'room number'}, inplace = True)

# 테스트 코드
df