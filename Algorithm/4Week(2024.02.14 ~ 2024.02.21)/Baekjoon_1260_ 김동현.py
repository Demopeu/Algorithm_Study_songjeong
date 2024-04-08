from collections import deque


def dfs(v):                                         # 재귀로 안풀면 순서 맞추기 귀찮아져서 이렇게 품
    visit[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if not visit[i] and graph[v][i]:            # 아래 graph를 1,2,3...N까지 볼 수 있도록 만들어서 and으로 저리 붙임
            dfs(i)


# 이걸로 하면 틀림 (pop으로 빼는 순서가 다르기 때문)
'''
def dfs(v):
    stack = [v]
    visited = [False] * (N + 1)
    visited[v] = True
    while stack:
        node = stack.pop()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
'''


def bfs(v):
    stack = deque([v])
    visited = [False]*(N+1)
    visited[v] = True

    while stack:
        node = stack.popleft()
        print(node,end = ' ')
        for i in range(1,N+1):
            if not visited[i] and graph[node][i]:
                visited[i] = True
                stack.append(i)


N,M,V = map(int,input().split())
graph = [[False]*(N+1) for _ in range(N+1)]                     # 1~N까지 순서대로 할 수 있도록 제작

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

visit = [False] * (N + 1)

dfs(V)
print()
bfs(V)

# https://www.acmicpc.net/problem/1260
# 이 코드의 시간 복잡도는 O(N^2)
# 모든 노드의 간선을 확인 해야 하므로 V*E인데 둘 다 N이므로