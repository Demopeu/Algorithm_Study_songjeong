import sys
import heapq

input = sys.stdin.readline
INF = float('inf')


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


n, m, k, x = map(int, input().split())  # n:도시 수, m: 도로 수, k: 거리 정보, x: 출발 도시 번호
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
k_cnt = 0

for _ in range(m):
    a, b = map(int, input().split())    # a: 출발지, b: 도착지
    graph[a].append([b, 1])

dijkstra(x)

for idx, value in enumerate(distance):
    if value == k:
        k_cnt += 1
        print(idx)

if k_cnt == 0:
    print(-1)


# 시간복잡도: O((n+m)logn)
# 출처: https://www.acmicpc.net/problem/18352