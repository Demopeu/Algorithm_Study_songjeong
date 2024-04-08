import heapq

def bfs(start, graph):
    q = []
    heapq.heappush(q, (0, start[0], start[1]))
    visited = [[0] * M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    limit = 0

    while q:
        depth, row, col = heapq.heappop(q)

        if (row, col) == target:
            return limit

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < M) or visited[nrow][ncol]:
                continue

            if i == 0 or i == 2:
                if graph[nrow][ncol]:
                    limit = max(limit, depth + 1)
                    visited[nrow][ncol] = 1
                    heapq.heappush(q, (0, nrow, ncol))
                else:
                    visited[nrow][ncol] = 1
                    heapq.heappush(q, (depth + 1, nrow, ncol))

            else:
                if depth:
                    continue

                if graph[nrow][ncol]:
                    visited[nrow][ncol] = 1
                    heapq.heappush(q, (0, nrow, ncol))

N, M = list(map(int, input().split()))
map_ = [list(map(int, input().split())) for _ in range(N)]
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]
limit = 0

for row in range(N):
    for col in range(M):
        if map_[row][col] == 2:
            start = (row, col)

        if map_[row][col] == 3:
            target = (row, col)

print(bfs(start, map_))