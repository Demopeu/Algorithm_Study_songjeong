import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def dfs(start, graph, visited):
    visited[start] = 1
    
    for i in graph[start]:
        if visited[i] == 0:             # 방문 안 한 곳이라면, dfs 재귀 호출
            dfs(i, graph, visited)

    return visited


n, m = map(int, input().split())        # 정점의 개수 n, 간선의 개수 m
graph = [[] for _ in range(n + 1)]      # 간선 리스트
visited = [0 for _ in range(n + 1)]     # 방문 node 체크 리스트
connected_component = 0

for _ in range(m):                      # 간선 인접 리스트 사용해서 추가
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)                  # 방향 없는 graph임으로 양쪽 다 추가

for node in range(1, n + 1):
    if visited[node] == 0:
        dfs(node, graph, visited)       # dfs 호출할 때마다 connected_component 1 증가
        connected_component += 1

print(connected_component)


# 시간복잡도: O(V + E)
# 출처: https://www.acmicpc.net/problem/11724