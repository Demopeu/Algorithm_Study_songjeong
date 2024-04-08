import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    total_cost[start] = 0
    while q:
        cos, now = heapq.heappop(q)
        if total_cost[now] < cos:
            continue
        for i in graph[now]:
            cost = i[1] + cos
            if cost < total_cost[i[0]]:
                total_cost[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


n = int(input())    # n: 도시의 수
m = int(input())    # m: 버스의 수
graph = [[] for _ in range(n + 1)]
total_cost = [float('inf') for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())     # s: 출발지, e: 도착지, c: 비용
    graph[s].append((e, c))

s_city, e_city = map(int, input().split())

dijkstra(s_city)
print(total_cost[e_city])


# 시간복잡도: O((n+m)logn)
# 출처: https://www.acmicpc.net/problem/1916