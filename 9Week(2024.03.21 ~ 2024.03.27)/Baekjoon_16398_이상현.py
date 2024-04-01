from heapq import *

def find_parent(parent, v):
    if parent[v] == v:
        return v
    return find_parent(parent, parent[v])

def union(parent, rank, v1, v2):
    root1 = find_parent(parent, v1)
    root2 = find_parent(parent, v2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskal(start):
    sum_ = 0
    parent = {}
    rank = {}

    for v in range(N):
        parent[v] = v
        rank[v] = 0

    heapify(graph)

    while graph:
        w, v1, v2 = heappop(graph)

        if find_parent(parent, v1) == find_parent(parent, v2):
            continue
        sum_ += w
        union(parent, rank, v1, v2)

    return sum_

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
graph = []

for i in range(N - 1):
    for j in range(i + 1, N):
        graph.append((list_[i][j], i, j))

print(kruskal(graph))

#Memory: 194192KB, RunTime: 3080ms
#href: https://www.acmicpc.net/problem/16398