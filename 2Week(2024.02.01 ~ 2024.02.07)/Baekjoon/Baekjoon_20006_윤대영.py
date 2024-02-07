p, m = map(int, input().split())    # p: 플레이어 수, m: 방의 정원, l: 레벨, n: 닉네임
server = []                         # room이 생성될 배열

for _ in range(p):
    l, n = input().split()
    l = int(l)

    if len(server) == 0:            # room이 하나도 없다면 만들고, 새 room에 추가
        server.append([])
        server[-1].append((l, n))
        continue
    elif len(server) > 0:           # room이 있다면, room을 돌면서 플레이어가 들어갈 room 찾기
        for room in server:
            if len(room) == m:
                continue
            elif len(room) >= 1 and (room[0][0] - 10 <= l <= room[0][0] + 10):    # room 첫 플레이어 레벨 확인 후 room에 추가
                room.append((l, n))
                break
        else:                       # for문을 다 돌았음에도 불구하고 들어갈 room이 없다면, 새 room에 추가
            server.append([])
            server[-1].append((l, n))

for room in server:
    room.sort(key=lambda x:x[1])    # n을 기준으로 room 정렬
    if len(room) == m:              # room이 꽉 찼다면,
        print('Started!')
        for p_info in room:
            print(*p_info)
    else:   
        print('Waiting!')           # room이 꽉 차지 않았다면,
        for p_info in room:
            print(*p_info)

# 시간 복잡도: O(p * m) - 일반적 상황, O(p^2) - 최악의 상황
# 출처: https://www.acmicpc.net/problem/20006