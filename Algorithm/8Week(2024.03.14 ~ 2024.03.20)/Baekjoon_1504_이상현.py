import sys
input = sys.stdin.readline

import heapq

def dijkstra(start, graph):
    q = []
    heapq.heappush(q, (0, start))
    cost_list[start] = 0

    while q:
        current_cost, current_vertex = heapq.heappop(q)

        if current_cost > cost_list[current_vertex]:
            continue

        for cost, vertex in graph[current_vertex]:
            temp = current_cost + cost

            if temp < cost_list[vertex]:
                cost_list[vertex] = temp
                heapq.heappush(q, (temp, vertex))

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cost_list = [float('inf')] * (N + 1)

for _ in range(E):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))

start, end = map(int, input().split())
dijkstra(1, graph)
temp1 = cost_list[start]

cost_list = [float('inf')] * (N + 1)
dijkstra(start, graph)
temp1 += cost_list[end]

cost_list = [float('inf')] * (N + 1)
dijkstra(end, graph)
temp1 += cost_list[N]

cost_list = [float('inf')] * (N + 1)
dijkstra(1, graph)
temp2 = cost_list[end]

cost_list = [float('inf')] * (N + 1)
dijkstra(end, graph)
temp2 += cost_list[start]

cost_list = [float('inf')] * (N + 1)
dijkstra(start, graph)
temp2 += cost_list[N]
min_ = min(temp1, temp2)

print(min_ if min_ != float('inf') else -1)