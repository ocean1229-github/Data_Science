import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 여기에 코드를 작성하세요

# 테스트 코드
df['status'] = 'allowed'
df.loc[(df['year'] == 1) & (df['course name'] == 'information technology'), 'status'] = 'not allowed'

df.loc[(df['year'] == 4) & (df['course name'] == 'commerce'), 'status'] = 'not allowed'

classMember = df['course name'].value_counts()
condition = classMember < 5
classlist = list(classMember[condition].index)
cut = df['course name'].isin(classlist)
df.loc[cut, 'status'] = 'not allowed'

df

# 모범답안
import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')
df["status"] = "allowed"

# 조건 1
boolean1 = df["course name"] == "information technology"
boolean2 = df["year"] == 1
df.loc[boolean1 & boolean2, "status"] = "not allowed"

# 조건 2
boolean3= df["course name"] == "commerce"
boolean4= df["year"] == 4
df.loc[boolean3& boolean4, "status"] = "not allowed"

# 조건 3
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"

# 테스트 코드
df
