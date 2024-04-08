import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (directions[0][0], start[0], start[1]))
    rupee[start[0]][start[1]] = directions[0][0]

    while q:
        lose, now_x, now_y = heapq.heappop(q)
        if lose > rupee[now_x][now_y]:
            continue
        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n:
                cost = lose + directions[new_x][new_y]
                if cost < rupee[new_x][new_y]:
                    rupee[new_x][new_y] = cost
                    heapq.heappush(q, (cost, new_x, new_y))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tc = 0

while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    directions = [list(map(int, input().split())) for _ in range(n)]
    rupee = [[INF for _ in range(n)] for _ in range(n)]
    dijkstra((0, 0))

    print(f'Problem {tc}: {rupee[n - 1][n - 1]}')


# 시간복잡도: O(n^2logn)
# 출처: https://www.acmicpc.net/problem/4485