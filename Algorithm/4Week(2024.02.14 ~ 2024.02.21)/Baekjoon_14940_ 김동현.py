from collections import deque


def bfs(start):
    queue = [[start, 0]]                                            # 2번째꺼는 new_matrix에 넣을 방문 수
    visited = [[False]*M for _ in range(N)]
    visited[start[0]][start[1]] = True
    queue = deque(queue)
    new_matrix = [[0]*M for _ in range(N)]                          # 새롭게 받을 메트릭스 만듬
    
    while queue:
        node = queue.popleft()
        new_matrix[node[0][0]][node[0][1]] = node[1]

        for l in range(4):

            nx = node[0][0] + dx[l]
            ny = node[0][1] + dy[l]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1: # or 안한건 귀찮았습니다...
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([[nx,ny],node[1]+1])

    return new_matrix


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(N):
    flag = False
    for j in range(M):
        if matrix[i][j] == 2:
            flag = True
            break
    if flag:
        break

answer = bfs([i, j])

for i in range(N):                                  # 만일 new matrix에 0이 진짜 0인지 못가서 0인지 판단
    for j in range(M):
        if answer[i][j] == 0:
            if matrix[i][j] == 1:
                answer[i][j] = -1

for i in range(N):
    print(*answer[i])

# 이 코드의 시간 복잡도는 O(N*M)
    # for 구문 두개니까 O(N*M)
    # bfs는 O(E)이므로
    # O(N*M + E) = O(N*M)