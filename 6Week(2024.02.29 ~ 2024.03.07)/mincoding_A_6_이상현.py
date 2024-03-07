from heapq import*

T = int(input())
drow, dcol = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(start, graph):
    q = []
    heappush(q, (0, start[0], start[1]))
    target = (N - 1, N - 1)

    while q:
        fuel, row, col = heappop(q)

        if fuel > min_list[row][col]:
            continue

        min_list[row][col] = fuel

        if (row, col) == target:
            return fuel

        # tunnel
        for tunnel in tunnel_list:
            if tunnel[5]:
                continue

            if (row, col) == (tunnel[0] - 1, tunnel[1] - 1):
                tunnel[5] = 1
                heappush(q, (fuel + tunnel[4], tunnel[2] - 1, tunnel[3] - 1))

            elif (row, col) == (tunnel[2] - 1, tunnel[3] - 1):
                tunnel[5] = 1
                heappush(q, (fuel + tunnel[4], tunnel[0] - 1, tunnel[1] - 1))

        # not tunnel
        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            if not (0 <= nrow < N and 0 <= ncol < N):
                continue

            temp1, temp2 = graph[row][col], graph[nrow][ncol]

            if temp1 > temp2:
                heappush(q, (fuel, nrow, ncol))

            elif temp1 < temp2:
                heappush(q, (fuel + 2 * (temp2 - temp1), nrow, ncol))

            else:
                heappush(q, (fuel + 1, nrow, ncol))

for tc in range(T):
    N, M = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(N)]
    tunnel_list = []
    min_list = [[float('inf')] * N for _ in range(N)]

    for _ in range(M):
        tunnel_list.append(list(map(int, input().split())) + [0])

    print(f'#{tc + 1} {bfs((0, 0), map_)}')