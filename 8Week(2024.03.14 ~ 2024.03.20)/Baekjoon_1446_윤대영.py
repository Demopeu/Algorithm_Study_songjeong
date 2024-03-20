import heapq

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    short_dis[s] = 0
    while q:
        dis, now = heapq.heappop(q)
        if dis > short_dis[now]:
            continue

        for i in graph[now]:
            cost = dis + i[1]
            if cost < short_dis[i[0]]:
                short_dis[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, d = map(int, input().split())    # n: 지름길 개수, d: 고속도로 길이
graph = [[] for _ in range(d + 1)]
short_dis = [float('inf') for _ in range(d + 1)]

for i in range(d):
    graph[i].append((i + 1, 1))

for _ in range(n):
    start, end, distance = map(int, input().split())
    if end > d:
        continue
    graph[start].append((end, distance))

dijkstra(0)
print(short_dis[d])


# 시간복잡도: O(dlogd)
# 출처: https://www.acmicpc.net/problem/1446