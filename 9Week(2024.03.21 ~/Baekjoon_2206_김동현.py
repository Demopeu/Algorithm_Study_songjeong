from collections import deque

def bfs(i,j,k):
    quque = deque([(i,j,k)])
    # i,j의 방문 횟수를 [0,0]으로 만듬
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[i][j][k] = 1
    while quque:
        i,j,k = quque.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][k]
            
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]
            
            # 두가지 평행 세계를 만들어 저장
            if 0<=nx <N and 0<=ny <M:
                # [0,0]에서 인덱스 0는 벽이 부셔지지 않았을때의 세계
                if matrix[nx][ny] == 1 and k == 0:
                    visited[nx][ny][1] = visited[i][j][k]+1
                    quque.append((nx,ny,1))
                # 인덱스 1은 벽이 부셔진 세계
                if matrix[nx][ny] == 0 and visited[nx][ny][k] == 0:
                    visited[nx][ny][k] = visited[i][j][k]+1
                    quque.append((nx, ny, k))
    return -1


N,M = map(int,input().split())
matrix = list(list(int(i) for i in input()) for _ in range(N))
dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(bfs(0,0,0))

# https://www.acmicpc.net/problem/2206
# 이 코드의 시간 복잡도는 O(N^2)

