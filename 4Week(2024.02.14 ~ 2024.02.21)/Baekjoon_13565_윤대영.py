import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x, y, matrix, visit):
    visit[x][y] = 1

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if temp_x < 0 or temp_x >= m or temp_y < 0 or temp_y >= n:      # 범위를 벗어나거나, pass
            continue
        if visit[temp_x][temp_y] == 1 or matrix[temp_x][temp_y] == 1:   # 이미 방문했거나 전류가 통하지 않을 경우, pass
            continue
        dfs(temp_x, temp_y, matrix, visit)


m, n = map(int, input().split())    # m: 세로, n: 가로
grid = [list(map(int, list(input()))) for _ in range(m)]    # 0: 전류 통하는 흰색, 1: 전류가 통하지 않는 검은색
visited = [[0 for _ in range(n)] for _ in range(m)]         # 방문 체크
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
flag = False
pr_flag = False

for r in range(1):
    for c in range(n):
        if grid[r][c] == 0:
            dfs(r, c, grid, visited)

for r in range(m - 1, m):
    for c in range(n):
        if visited[r][c] == 1 and grid[r][c] == 0:          # 방문했고, 전류가 통하는 곳이라면
            pr_flag = True
            flag = True
            break
    if flag:
        break

if pr_flag:
    print('YES')
else:
    print('NO')


# 시간복잡도: O(MN)
# 출처: https://www.acmicpc.net/problem/13565