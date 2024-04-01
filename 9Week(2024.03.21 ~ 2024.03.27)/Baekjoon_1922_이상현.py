from heapq import *

def prim(start):
    connected = {start}
    unconnected = [(w, v) for v, w in graph[start]]
    heapify(unconnected)
    sum_ = 0

    while unconnected:
        weight, vertex = heappop(unconnected)

        if vertex in connected:
            continue

        connected.add(vertex)
        sum_ += weight

        for v, w in graph[vertex]:
            if v in connected:
                continue
            heappush(unconnected, (w, v))

    return sum_

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(1))

#Memory: 130024KB, RunTime: 396ms
#href: https://www.acmicpc.net/problem/1922