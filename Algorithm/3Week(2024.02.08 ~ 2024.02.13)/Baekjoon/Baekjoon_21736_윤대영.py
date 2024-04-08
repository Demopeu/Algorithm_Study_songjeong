import sys

sys.setrecursionlimit(10 ** 8)              # 재귀 최대 깊이 제한 변경

def dfs(matrix, visited, x, y):
    global p_cnt
    n, m = len(matrix), len(matrix[0])              # 행렬 행, 열 길이
    
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:    # 범위 벗어나면 return False
        return False
    if matrix[x][y] == 'X':                 # matrix[x][y] == 벽이라면 return False
        return False
    if  visited[x][y] == 0:                 # 방문 안한 곳이라면, 방문 체크 후 상하좌우 재귀 호출
        visited[x][y] = 1
        if matrix[x][y] == 'P':
            p_cnt += 1
        dfs(matrix, visited, x + 1, y)
        dfs(matrix, visited, x - 1, y)
        dfs(matrix, visited, x, y - 1)
        dfs(matrix, visited, x, y + 1)

    return True

n, m = map(int, input().split())
matrix = [list(input()) for r in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
p_cnt = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'I':     # 도연이 위치 파악 후, break
            pos_x, pos_y = i, j
            break

dfs(matrix, visited, pos_x, pos_y)

if p_cnt == 0:
    print('TT')
else:
    print(p_cnt)

# 시간복잡도: O(N * M)
# 출처: https://www.acmicpc.net/problem/21736