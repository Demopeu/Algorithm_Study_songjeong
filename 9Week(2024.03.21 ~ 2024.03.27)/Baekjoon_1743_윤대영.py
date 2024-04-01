import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def dfs(x, y):
    cnt = 1
    visited[x][y] = 1

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m:
            if visited[tx][ty] == 0 and aisle[tx][ty] == 1:
                cnt += dfs(tx, ty)
    return cnt


n, m, k = map(int, input().split())    # n: 세로, m: 가로, k: 음식물 수
aisle = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_size = -sys.maxsize

for _ in range(k):
    r, c = map(int, input().split())
    aisle[r - 1][c - 1] = 1

for i in range(n):
    for j in range(m):
        if aisle[i][j] == 1 and visited[i][j] == 0:
            size = dfs(i, j)
            if size > max_size:
                max_size = size

print(max_size)


# 시간복잡도: O(V + E)
# 출처: https://www.acmicpc.net/problem/1743