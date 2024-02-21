# 백준 6118번 숨바꼭질

from collections import deque

# 주어진 정점에서 가장 멀리 있는 정점 (여러 개라면 작은 번호를 가진 정점),
# 그 정점까지의 거리, 같은 거리를 갖는 정점의 개수를 구하는 문제
def bfs(start, graph):
    q = deque()
    q.append((start, 0))
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        # vertex는 현재 정점, cnt는 현재 정점까지의 거리
        vertex, cnt = q.popleft()

        for v in graph[vertex]:
            # 방문하지 않은 인접 정점이 존재한다면 cnt + 1을 하고
            # 탐색, visited 배열에 방문 표시 + 시작 정점과의 거리를 저장
            if not visited[v]:
                q.append((v, cnt + 1))
                visited[v] = cnt + 1

    return cnt, visited

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

cnt, visited = bfs(1, graph)
# visited[1] = 1을 하면 시작 정점과의 거리가 1인
# 경우에 시작 정점이 포함되기 때문에 0으로 저장
visited[1] = 0

# 가장 멀리 있는 정점 중 가장 번호가 작은 정점, 그 정점까지의 거리
# 그 거리를 갖는 정점의 개수를 출력
print(visited.index(cnt), cnt, visited.count(cnt))

# 문제링크 : https://www.acmicpc.net/problem/6118
# 시간복잡도 : O(V + E)
# 38408 KB, 2040 ms (;;) Python 3
# 117052 KB, 216 ms PyPy 3