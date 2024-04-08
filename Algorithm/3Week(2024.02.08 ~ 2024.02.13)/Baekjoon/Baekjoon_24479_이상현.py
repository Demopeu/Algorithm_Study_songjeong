import sys
sys.setrecursionlimit(300000)

# 백준 24479번 알고리즘 수업 - 깊이 우선 탐색 1
# 이 문제는 정점과 그 정점들간의 연결 관계가 주어졌을 때
# 각 정점의 방문 순서를 구하는 것이 목표

def dfs(start, graph, visited):
    global order

    # 방문 순서 설정
    order += 1
    visited[start] = order

    # 각 정점의 인접점에서 그 점을 방문하지 않았다면 함수를 재귀적으로 호출
    for vertex in graph[start]:
        if not visited[vertex]:
            dfs(vertex, graph, visited)

N, M, R = map(int ,input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

# 정점 간의 관계를 입력받아 그래프에 반영
for _ in range(M):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

# 인접점이 여러 개일 경우 오름차순으로 방문
for list_ in graph:
    list_.sort()

order = 0
dfs(R, graph, visited)

for i in range(1, N + 1):
    print(visited[i])

# 링크 : https://www.acmicpc.net/problem/24479