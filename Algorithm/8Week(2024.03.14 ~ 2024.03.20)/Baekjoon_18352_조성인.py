# https://www.acmicpc.net/problem/18352

# 시간초과 -> PyPy3 해결
from collections import deque

# 도시 수, 도로 수, 거리, 출발점
N,M,K,X = map(int,input().split())
# 도로 정보
nodes = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    nodes[A].append(B)

# 거리
distance = [0] * (N+1)
# 방문지
visited = [0] * (N+1)

# 큐 사용
q = deque()
q.append(X)
visited[X] = 1

result = []
# DFS
while q:
    now = q.popleft()
    # 현재 위치와 연결된 도로들
    destinations = nodes[now]
    for destination in destinations:
        # 방문하지 않은 곳일때
        if not visited[destination]:
            # 방문처리
            visited[destination] = 1
            # 해당 위치 큐에 추가
            q.append(destination)
            # 거리 + 1
            distance[destination] = distance[now] + 1
            # 목표거리이면 결과 리스트에 추가
            if distance[destination] == K:
                result.append(destination)

if result:
    # 정렬이 있었다...
    result.sort()
    for r in result:
        print(r)
# 결과가 없으면 -1 출력
else:
    print(-1)

