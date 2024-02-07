# https://www.acmicpc.net/problem/20006

# 시간 복잡도 : O(p)

# 플레이어의 수, 매칭 정원
p, m = map(int,input().split())

# 전체 서버
room_list = []
for i in range(p):
    # 레벨, 닉네임
    l, n = input().split()
    # l은 정수
    l = int(l)
    
    # 서버에 방이 없으면 방을 추가
    if len(room_list) == 0:
        room_list.append([[l,n]])

    else:
        # 방을 순회
        for room in room_list:
            # 플레이어와 해당 방의 플레이어의 레벨 차가 10 이하이고 방 정원이 다 차지 않았다면
            if abs(l - room[0][0]) <= 10 and len(room) < m:
                # 방에 추가
                room.append([l,n])
                break
            else:
                # 방을 다 돌았는데도 못 들어갔다면
                if room == room_list[-1]:
                    # 새 방을 만들기
                    room_list.append([[l,n]])
                    # 순회를 멈추지 않으면 만들어진 새 방에서 한번 더 돈다.
                    break

for room in room_list:
    # 각 방을 닉네임 순으로 정렬 : 유저 = [레벨, 닉네임]
    room = sorted(room, key=lambda x: x[1])
    # 정원이 다 찬 경우 요구사항에 맞게 출력
    if len(room) == m:
        print('Started!')
        for user in room:
            print(f'{user[0]} {user[1]}')
    # 아닌 경우 요구사항에 맞게 출력
    else:
        print('Waiting!')
        for user in room:
            print(f'{user[0]} {user[1]}')