import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 여기에 코드를 작성하세요
df['room assignment'] = 'not assigned'
classMember = df['course name'].value_counts()

# 1번 조건
auditorium_cond = list(classMember[classMember >= 80].index)
large_cond = list(classMember[(classMember >= 40) & (classMember < 80)].index)
medium_cond = list(classMember[(classMember >= 15) & (classMember < 40)].index)
small_cond = list(classMember[(classMember >= 5) & (classMember < 15)].index)

df.loc[df['course name'].isin(auditorium_cond), 'room assignment'] = 'Auditorium'
df.loc[df['course name'].isin(large_cond), 'room assignment'] = 'Large room'
df.loc[df['course name'].isin(medium_cond), 'room assignment'] = 'Medium room'
df.loc[df['course name'].isin(small_cond), 'room assignment'] = 'Small room'
df.loc[df['status'] == 'not allowed', 'room assignment'] = 'not assigned'

# 테스트 코드
df


#--------------------
# 모범답안
import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# not allowed 과목에 대해 값 지정해주기
not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

# allowed 과목에 대해 값 지정해주기
for course in auditorium_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"

for course in large_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
    
for course in medium_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
    
for course in small_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"
    
# 정답 출력
df
