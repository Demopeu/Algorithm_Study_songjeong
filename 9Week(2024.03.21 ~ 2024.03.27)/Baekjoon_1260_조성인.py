# https://www.acmicpc.net/problem/1260

from collections import deque

N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]

# 양방향 그래프
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 그래프 내부 정렬
for i in range(N+1):
    graph[i].sort()

dfs = {V}
bfs = {V}

# BFS용 큐 사용
queue = deque()
queue.append(V)

# DFS 부분인데 반복문으로는 잘 모르겠다.
# 같은 깊이에서 앞을 탐색해야되는데 뒤를 탐색해서 화나서 재귀로 바꿈
# print(V,end=' ')
# while stack:
#     now = stack.pop()
#     for i in graph[now]:
#         if i not in dfs:
#             dfs.add(i)
#             stack.append(i)
#             print(i, end=' ')

# DFS
# 사실 편한건 재귀가 아닌가
def DFS(num):
    print(num, end=' ')
    for i in graph[num]:
        if i not in dfs:
            dfs.add(i)
            DFS(i)

DFS(V)

# 줄바꿈용 프린트
print()

# BFS
print(V,end=' ')
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if i not in bfs:
            bfs.add(i)
            queue.append(i)
            print(i, end=' ')