# 백준 1244번 스위치 켜고 끄기

# 스위치들의 처음 상태
num_of_switch = int(input())
switch_list = list(map(int, input().split()))

# 각 학생의 성별과 받은 번호
num_of_student = int(input())
student_list = []

for _ in range(num_of_student):
    student_list.append(list(map(int, input().split())))

for student in student_list:
    # 만약 학생이 남학생이라면 자기가 받은 번호의 
    # 배수인 스위치의 상태를 바꿈
    if student[0] == 1:
        for i in range(num_of_switch):
            if (i + 1) % student[1] == 0:
                switch_list[i] = +(not switch_list[i])

    # 만약 학생이 여학생이라면 자기가 받은 번호를 중심으로 스위치 상태가
    # 좌우로 대칭인 최대인 구간에 속한 스위치의 상태를 바꿈
    else:
        # 자기 자신은 홀로 좌우대칭을 만족함
        temp = [student[1]]

        for i in range(1, num_of_switch):
            try:
                # 만약 좌우 대칭이면 그 번호를 temp에 저장
                if student[1] - i - 1 >= 0 and switch_list[student[1] - i - 1] == switch_list[student[1] + i - 1]:
                    temp.append(student[1] - i)
                    temp.append(student[1] + i)

                else:
                    break

            # 좌우를 탐색하다 인덱스를 벗어나면 반복문을 멈춤
            except IndexError:
                break

        # 대칭인 구간에 속한 스위치들의 상태를 바꿔줌
        for j in temp:
            switch_list[j - 1] = +(not switch_list[j - 1])

for i, state in enumerate(switch_list):
    print(state, end = ' ')

    # 문제의 조건에서 한 줄에 20개씩 출력
    if (i + 1) % 20 == 0:
        print()

# https://www.acmicpc.net/problem/1244