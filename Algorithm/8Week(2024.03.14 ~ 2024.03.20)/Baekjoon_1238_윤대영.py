import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


n, m, x = map(int, input().split())     # n: 학생 수, m: 도로 수, x: 도착지
graph = [[] for _ in range(n + 1)]
total_lst = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

for j in range(1, n + 1):
    total_lst[j] = dijkstra(j)[x] + dijkstra(x)[j]      # n번에서 x번까지의 거리 + x번에서 n번까지의 거리

print(max(total_lst))


# 시간복잡도: O((V+E)logV)
# 출처: https://www.acmicpc.net/problem/1238