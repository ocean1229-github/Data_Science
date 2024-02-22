import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 여기에 코드를 작성하세요
room_list = df.loc[df['status'] == 'allowed', 'room assignment'].unique()

# 조건 1
for room in room_list:
    course_list = sorted(df.loc[df['room assignment'] == room, 'course name'].unique())
    
    i = 1
    for course in course_list:
        df.loc[(df['course name'] == course) & (df['status']=='allowed'), 'room assignment'] = room.split()[0] + '-' + str(i)
        i += 1

# 조건 2
not_assigned = df['status'] == 'not allowed'
df.loc[not_assigned, 'room assignment'] = 'not assigned'

# 조건 3
df.rename(columns = {'room assignment' : 'room number'}, inplace = True)

# 테스트 코드
df


# 모범 답안
import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# 강의실 이름 붙이기
for i in range(len(auditorium_list)):
    df.loc[(df["course name"] == sorted(auditorium_list)[i]) & allowed, "room assignment"] = "Auditorium-" + str(i + 1)

for i in range(len(large_room_list)):
    df.loc[(df["course name"] == sorted(large_room_list)[i]) & allowed, "room assignment"] = "Large-" + str(i + 1)
    
for i in range(len(medium_room_list)):
    df.loc[(df["course name"] == sorted(medium_room_list)[i]) & allowed, "room assignment"] = "Medium-" + str(i + 1)
    
for i in range(len(small_room_list)):
    df.loc[(df["course name"] == sorted(small_room_list)[i]) & allowed, "room assignment"] = "Small-" + str(i + 1)

# column 이름 바꾸기
df.rename(columns={"room assignment": "room number"}, inplace = True)
    
# 테스트 코드
df

