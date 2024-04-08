import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x, y, matrix, visit):
    visit[x][y] = 1

    for i in range(8):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:      # 좌표 범위를 벗어나면 pass
            continue
        if visit[temp_x][temp_y] == 1 or matrix[temp_x][temp_y] == 0:   # 이미 방문했거나, 갈 수 없는 곳이라면 pass
            continue
        dfs(temp_x, temp_y, matrix, visit)


n, m = map(int, input().split())    # n: 세로 길이, m: 가로 길이
banner = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]    # 상하좌우, 4방향 대각선
dy = [0, 0, 1, -1, 1, -1, 1, -1]
result = 0

for r in range(n):
    for c in range(m):
        if banner[r][c] == 1 and visited[r][c] == 0:
            dfs(r, c, banner, visited)
            result += 1

print(result)


# 시간복잡도: O(NM)
# 출처: https://www.acmicpc.net/problem/14716