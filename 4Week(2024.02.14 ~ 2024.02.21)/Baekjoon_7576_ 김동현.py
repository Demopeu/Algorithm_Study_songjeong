from collections import deque


def bfs(queue):
    queue = deque(queue)
    max_count = 0                                                       # node = [[x,y],count] 느낌으로 짜봄 그래서 max_count
    while queue:
        node = queue.popleft()
        max_count = max(node[1],max_count)

        for l in range(4):

            nx = node[0][0] + dx[l]
            ny = node[0][1] + dy[l]

            if 0<= nx < N and 0<= ny < M and matrix[nx][ny] == 0:
                    matrix[nx][ny] = 1
                    queue.append([[nx,ny],node[1]+1])

    return max_count


# 변수
M,N = map(int,input().split())
matrix = [list(map(int,input().split()))for _ in range(N)]
queue = []

# 마지막 익은것의 유무를 판별
flag = False

# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            queue.append([[i,j],0])                                             #처음 친구들은 0으로

answer = bfs(queue)

# 만일 matrix에 안익은 친구가 있다면 -1로
for i in range(N):                                                              
    for j in range(M):
        if matrix[i][j] == 0:
            flag = True
            break
    if flag:
        break

# 결과문
print(-1 if flag else answer)