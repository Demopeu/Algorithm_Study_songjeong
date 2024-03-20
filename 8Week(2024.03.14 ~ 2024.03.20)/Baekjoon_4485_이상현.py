import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def dfs(row, col, cost):
    global min_

    if cost > min_:
        return

    if (row, col) == (N - 1, N - 1):
        min_ = min(min_, cost)

    for i in range(4):
        nrow, ncol = row + drow[i], col + dcol[i]

        if not (0 <= nrow < N and 0 <= ncol < N):
            continue

        if cost + list_[nrow][ncol] >= cost_list[nrow][ncol]:
            continue

        cost_list[nrow][ncol] = cost + list_[nrow][ncol]
        dfs(nrow, ncol, cost_list[nrow][ncol])

tc = 1
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]

while True:
    N = int(input())

    if not N:
        break

    list_ = [list(map(int, input().split())) for _ in range(N)]
    cost_list = [[float('inf')] * N for _ in range(N)]
    cost_list[0][0] = list_[0][0]
    min_ = float('inf')
    dfs(0, 0, list_[0][0])

    print(f'Problem {tc}: {min_}')
    tc += 1