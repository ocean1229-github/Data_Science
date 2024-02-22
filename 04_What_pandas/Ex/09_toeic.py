import pandas as pd
    
df = pd.read_csv('data/toeic.csv')

# 여기에 코드를 작성하세요
df['합격 여부'] = (df['LC'] + df['RC'] >= 600) & (df['LC'] >250) & (df['RC']>250)

# 테스트 코드
df