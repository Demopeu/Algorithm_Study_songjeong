from heapq import *

def dijkstra(start):
    q = []
    heappush(q, (0, start))

    while q:
        time, vertex = heappop(q)

        if time > time_list[vertex]:
            continue

        for ntime, v in graph[vertex]:
            if time + ntime < time_list[v]:
                time_list[v] = time + ntime
                heappush(q, (time_list[v], v))

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
time_list = [float('inf')] * (N + 1)

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

graph1 = [elem[:] for elem in graph]

dijkstra(X)
time_list[X] = 0
result = time_list[:]

for i in range(1, N + 1):
    if i == X:
        continue
    time_list = [float('inf')] * (N + 1)
    dijkstra(i)
    result[i] += time_list[X]

print(max(result[1:]))