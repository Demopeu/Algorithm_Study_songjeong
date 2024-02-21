# https://www.acmicpc.net/problem/2178

# 시간복잡도 : O(N * M)

from collections import deque

N,M = map(int,input().split())
# 미로를 문자열로 받는다.
# 1부터 매핑할건데 1을 매핑하면 겹치기 때문에 타입으로 지나간 곳을 구분하려 함
maze = [list(input()) for _ in range(N)]

# 큐 사용(bfs)
q = deque()
q.append([0,0])

# 늘 보던 그거
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 처음 시작은 1부터 시작(문자열 '1' => 정수)
maze[0][0] = 1
while q:
    [x,y] = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # isinstance(변수,타입) : 변수와 타입이 맞으면 True, 아니면 False
        if 0 <= nx < M and 0 <= ny < N and isinstance(maze[ny][nx],str) and maze[ny][nx] == '1':
            # num이라는 변수를 사용하지 않고 그냥 앞의 좌표에서 +1
            # while 바로 밑에서 하는 것보다 여기서 바꾸는 게 더 좋다고 한다.
            maze[ny][nx] = maze[y][x] + 1
            q.append([nx,ny])

# 미로의 목표지점을 출력
print(maze[N-1][M-1])