# 백준 2644번 촌수계산

from collections import deque

# 두 정점간의 거리를 구하는 문제
def bfs(start, end, graph):
    q = deque()
    q.append((start, 0))
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        # vertex는 현재 정점, cnt는 시작 정점부터 현재 정점까지의 거리
        vertex, cnt = q.popleft()

        # 우리가 찾는 목표라면 반복문 종료
        if vertex == end:
            break

        for v in graph[vertex]:
            # 만약 방문하지 않은 인접 정점이 존재한다면
            # cnt를 1 증가시키고 탐색 시작
            if not visited[v]:
                q.append((v, cnt + 1))
                visited[v] = 1

    # 만약 목표를 찾았다면 cnt를 반환하고, 아니라면 -1을 반환 후 출력
    return cnt if visited[end] else -1

n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())

    # 양방향 그래프
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(start, end, graph))

# 문제링크 : https://www.acmicpc.net/problem/2644
# 시간복잡도 : O(V + E)
# 34044 KB, 64 ms