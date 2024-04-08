from collections import deque

# 시간복잡도 : O(n * m)

n,m = map(int,input().split())
matrix = [list(input().split()) for _ in range(n)]

# 늘 먹던 그 방향
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# BFS라 큐 사용
queue = deque()

# 시작 지점인 '2'를 찾아서 큐에 넣음
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '2':
            matrix[i][j] = 0
            queue.append([j, i])
            break

# 큐가 존재하는 동안(계속 나아가는 동안) 반복
while queue:
    # 큐에서 좌표를 꺼내고
    [x,y] = queue.popleft()
    # 4방향으로 다음 좌표 확인
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 지도 안에 있고 갈 수 있으면
        if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == '1':
            # 큐에 추가
            queue.append([nx,ny])
            # 이전 칸에서 +1
            matrix[ny][nx] = matrix[y][x] + 1

# 문자열로 받았으므로 제출 양식에 맞게 변경
for i in range(n):
    for j in range(m):
        if matrix[i][j] == '1':
            matrix[i][j] = -1
        if matrix[i][j] == '0':
            matrix[i][j] = 0

# 출력도 리스트로 했으면 좋겠다
for i in range(n):
    print(*matrix[i])