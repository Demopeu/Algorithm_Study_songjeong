# https://www.acmicpc.net/problem/5014

# 시간복잡도 : O(F)

from collections import deque

F,S,G,U,D = map(int,input().split())

# 빌딩
building = [0] * F

# BFS라 큐 사용
queue = deque()
queue.append(S-1)

# 가야되는 층이 같으면 안 누름
# 그럴거면 엘리베이터 왜 타...?
if S == G:
    print(0)
else:
    while queue:
        now = queue.popleft()
        # 원래는 안 썼는데 첫층에 방문표시하려고 빼놓음
        count = building[now]
        # 첫층에 방문표시 visited는 죽어도 쓰고 싶지 않다는 마음가짐
        if now == S-1:
            building[now] = -1
        # 위로 올라가는 경우와 아래로 내려가는 경우
        up = now + U
        down = now - D
        # 건물을 안뚫고 안 간 곳이면 1씩 추가하고 큐에 추가
        if up < F and building[up] == 0:
            building[up] = count + 1
            # 뒤늦게 조건 생각 나서 추가(조건 달성시 반복 중단)
            if up == G-1:
                break
            queue.append(up)
        if down >= 0 and building[down] == 0:
            building[down] = count + 1
            # 뒤늦게 조건 생각 나서 추가(조건 달성시 반복 중단)
            if down == G-1:
                break
            queue.append(down)
    
    # 같은 층인 경우가 아닐 때 결과에 따라 출력
    if building[G-1]:
        print(building[G-1])
    else:
        print('use the stairs')