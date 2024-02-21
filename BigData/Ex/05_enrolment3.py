import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 여기에 코드를 작성하세요

# 조건 1
sorted(df['room assignment'])
auditorium_count = len(list(df['room assignment'] == 'Auditorium'].index))

#"room number" 컬럼에는 Auditorium, Large room, Medium room, Small room, Not assigned 값들이 있음.
#오름차순으로 리스트에 넣어줌
df['room number'].value_counts().index
room = list(df['room number'].value_counts().index)
room.sort()

#room number 컬럼에 '강의실종류 + 번호'방식으로 값들을 만들어 'course name'별로 할당시키기 위한 리스트
room_detail = ['Auditorium-', 'Large-', 'Medium-', 'Small-']


#방종류별로 거기에 맞는 강의종류들을 list로 뽑고, 알파벳 순서대로 '강의실종류 + 번호' 방식의 강의실 번호를 부여합니다.

for i in range(4):
    course_name_list = list(df.loc[df['room number'] == room[i], 'course name'].value_counts().index)
    course_name_list.sort()
    for j in range(len(course_name_list)):
        df.loc[df['course name'] == course_name_list[j], 'room number'] = '%s%d' %(room_detail[i], j+1)
df


# 조건 2
not_assigned = df['status'] == 'not allowed'
df.loc[not_assigned, 'room assignment'] = 'not assigned'

# 조건 3
df.rename(columns = {'room assignment' : 'room number'}, inplace = True)

# 테스트 코드
df