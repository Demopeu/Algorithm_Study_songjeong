# 반복문을 이용한 dfs
def dfs(x,y,matrix_s,visit,colors):
    stack = list([x,y])                                                     # 첫 스텍

    while stack:

        node = stack.pop()

        if not visit[node[0]][node[1]] :                                    # 방문 안한 거 체크 후 방문으로 변경
            visit[node[0]][node[1]] = True

            for l in range(4):                                              # 상하좌우 확인
                new_i = node[0] + dx[l]
                new_j = node[1] + dy[l]

                if 0 <= new_i < N and 0 <= new_j < N and matrix_s[new_i][new_j] == colors:  # 같은 색깔이면 stack에 넣어
                    stack.append([new_i,new_j])


# 변수 및 정상과 색약을 따로 만듬
N = int(input())
matrix = [input() for _ in range(N)]
matrix_GB = [['R' if matrix[i][j] == 'G' else matrix[i][j] for j in range(N)] for i in range(N)]

# 방문확인도 두개
visited = [[False]*N for _ in range(N)]
visited_GB = [[False]*N for _ in range(N)]
count = 0
count_GB = 0

# 상하좌우 좌표
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 색깔 확인 후 dfs
for i in range(N):
    for j in range(N):
        
        color = matrix[i][j]                                        # 정상 색깔 확인
        color_GB = matrix_GB[i][j]                                  # 색약 색깔 확인
        
        if not visited[i][j] and matrix[i][j] == color:             # 정상 dfs 진입문
            count += 1
            dfs(i,j,matrix,visited,color)
            
        if not visited_GB[i][j] and matrix_GB[i][j] == color_GB:    # 색약 dfs 진입문
            count_GB += 1
            dfs(i,j,matrix_GB,visited_GB,color_GB)

# 결과문
print(f'{count} {count_GB}')

# 이 코드의 시간 복잡도는 O(N^2)
    # 4방향 이동을 정점당 하기 때문에 시간 복잡도인 O(V+E)
    # 이때 정점 수는 N^2, 간선 수는 4*N^2
    # 따라서 O(N^2)

# 재귀 함수를 이용한 dfs
'''
import sys
sys.setrecursionlimit(10**6)                # 재귀 깊이 변화해줘도 재귀 깊이 초과 오류남

def dfs(x,y,matrix_s,visit,colors):
    visit[x][y] = True

    for l in range(4):
        new_i = x + dx[l]
        new_j = y + dy[l] 

        if 0 <= new_i < N and 0 <= new_j < N and matrix_s[new_i][new_j] == colors:
                    dfs(new_i,new_j,matrix_s,visit,colors)

'''












