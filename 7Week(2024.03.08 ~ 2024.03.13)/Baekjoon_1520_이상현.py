import sys
sys.setrecursionlimit(100000)

def dfs(row, col):
    if m[row][col] != -1:
        return m[row][col]

    if row == M - 1 and col == N - 1:
        return 1

    cnt = 0

    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]

        if not (0 <= nrow < M and 0 <= ncol < N) or list_[row][col] <= list_[nrow][ncol]:
            continue

        cnt += dfs(nrow, ncol)

    m[row][col] = cnt
    return cnt

M, N = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(M)]
m = [[-1] * N for _ in range(M)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]

dfs(0, 0)
print(dfs(0, 0))