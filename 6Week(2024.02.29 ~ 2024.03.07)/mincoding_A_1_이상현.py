from collections import deque

def bfs(row, col, m, cnt, direction):
    global start, d
    
    q = deque()
    q.append((row, col, cnt, direction))

    while q:
        row, col, cnt, direction = q.popleft()

        if list_[row][col] == m:
            start = (row, col)
            d = direction
            return cnt

        for i in [direction % 4, (direction + 1) % 4]:
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < N):
                continue

            if i == direction % 4:
                q.append((nrow, ncol, cnt, i))
            else:
                q.append((nrow, ncol, cnt + 1, i))

T = int(input())
drow, dcol = [0, 1, 0, -1], [1, 0, -1, 0]

for tc in range(T):
    N = int(input())
    list_ = [list(map(int, input().split())) for _ in range(N)]
    M = max(max(row) for row in list_)
    result = d = 0
    start = (0, 0)

    for m in range(1, M + 1):
        result += bfs(start[0], start[1], m, 0, d)

    print(f'#{tc + 1} {result}')