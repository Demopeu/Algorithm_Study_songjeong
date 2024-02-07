import sys
input = sys.stdin.readline

p,m = map(int,input().split())
lst = [[]for _ in range(p)]                                             # 혹시 레벨이 전부 다를 수 있으니 사람 수만큼 미리 방 만듬

for _ in range(p):
    level,n = map(str,input().split())                                  # 이거 그냥 input으로 받으면 10번 줄 줄일 수 있을까?
    i = 0                                                               # 1번 방부터 탐색하려고
    level = int(level)
    while True:
        if lst[i] == []:                                                # 빈 방이면 첫사람 입장
            lst[i].append([level,n])
            break
        if lst[i][0][0]-10<=level<=lst[i][0][0]+10 and len(lst[i])<m:   # 사람 있으면, 첫사람한테 맞추고, 인원 수 맞추고
            lst[i].append([level, n])
            break
        i += 1                                                          # 조건 안맞으면 다음 방으로
for k in lst:
    if len(k) == m:                                                     # 방 다 채웠으면 시작
        print('Started!')
        sorted_lst = sorted(k,key=lambda x:x[1])                        # 알파벳 순으로
        for l in sorted_lst:
            print(*l)
    elif len(k) != 0:                                                   # 빈 방이 아니고 방을 다 못채웠을 경우
        print('Waiting!')
        sorted_lst = sorted(k, key=lambda x: x[1])
        for l in sorted_lst:
            print(*l)

# https://www.acmicpc.net/problem/20006
            
# 이 코드의 시간 복잡도는 O(N*log(N))
            # 반복문을 p만큼 돌아야 하고 각 방당 인원 수 m에 따라 달라짐
            # 따라서 내부 반복은 O(p*m)
            # 정렬을 하기 때문에 O(log(N))
            # 따라서 O(N*log(N))