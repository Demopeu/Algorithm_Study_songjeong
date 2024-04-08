import sys
sys.setrecursionlimit(100000)

def dfs(row, col):
    global max_

    if m[row][col] != 0:
        return m[row][col]

    m[row][col] = 1

    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]

        if not (0 <= nrow < n and 0 <= ncol < n):
            continue

        if list_[row][col] >= list_[nrow][ncol]:
            continue

        m[row][col] = max(m[row][col], 1 + dfs(nrow, ncol))

    return m[row][col]

max_ = 0
n = int(input())
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]

list_ = [list(map(int, input().split())) for _ in range(n)]
m = [[0] * n for _ in range(n)]

for row in range(n):
    for col in range(n):
        max_ = max(max_, dfs(row, col))

print(max_)
