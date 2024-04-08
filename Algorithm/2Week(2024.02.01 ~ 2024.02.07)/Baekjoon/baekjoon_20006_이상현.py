# 백준 20006번 랭킹전 대기열

p, m = map(int, input().split())

# 방들을 저장할 리스트 생성
rooms = []

for i in range(p):
    player = input().split()

    # 만약 생성된 방들 중 플레이어가 들어갈 수 있는 방이 존재한다면
    # [player의 닉네임, player의 레벨]과 같이 리스트의 형태로 저장
    for room in rooms:
        if room[0] <= int(player[0]) <= room[1] and len(room) < 2 + m:
            room.append([player[1], player[0]])
            break

    # 만약 플레이어가 들어갈 수 있는 방이 존재하지 않는다면 새로운 방을 생성
    # 여기서 각 방의 첫 번재 원소와 두 번째 원소는 방에 입장할 수 있는 레벨의
    # 범위를 나타냄
    else:
        rooms.append([int(player[0]) - 10, int(player[0]) + 10, [player[1], player[0]]])

# 만들어진 방들마다 만약 방이 꽉 차있으면 Started, 그렇지 않으면 Waiting을
# 출력하고 player의 닉네임 순으로 정렬 후 레벨과 함께 출력함
for room in rooms:
    temp = sorted(room[2:])

    print('Started!' if len(temp) == m else 'Waiting!')

    for player_info in temp:
        print(*player_info[::-1])

# https://www.acmicpc.net/problem/20006