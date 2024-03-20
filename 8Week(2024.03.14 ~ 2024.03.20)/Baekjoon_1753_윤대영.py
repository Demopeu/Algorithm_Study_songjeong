import sys
import heapq

input = sys.stdin.readline
INF = float('Inf')

def dijkstra(start):
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


v, e = map(int, input().split())    # v: 정점의 개수, e: 간선의 개수
s = int(input())    # 시작 정점 번호
graph = [[] for _ in range(v + 1)]
distance = [INF for _ in range(v + 1)]

for _ in range(e):
    u, v, w = map(int, input().split())     # u: 출발지, v: 도착지, w: 가중치(거리)
    graph[u].append([v, w])

dijkstra(s)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)


# 시간복잡도: O((V+E)logV)
# 출처: https://www.acmicpc.net/problem/1753