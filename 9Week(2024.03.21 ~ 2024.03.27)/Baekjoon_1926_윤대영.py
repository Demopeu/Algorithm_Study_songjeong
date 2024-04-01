import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    width = 1
    visited[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m and visited[tx][ty] == 0 and drawings[tx][ty] == 1:
            width += dfs(tx, ty)
    return width


n, m = map(int, input().split())    # n: 세로, m: 가로
drawings = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_width = 0
draw_cnt = 0

for r in range(n):
    for c in range(m):
        if drawings[r][c] == 1 and visited[r][c] == 0:
            width = dfs(r, c)
            draw_cnt += 1
            if width > max_width:
                max_width = width

print(draw_cnt)
print(max_width)


# 시간복잡도: O(V + E)
# 출처: https://www.acmicpc.net/problem/1926