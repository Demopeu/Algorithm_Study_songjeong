# https://www.acmicpc.net/problem/1697

from collections import deque

N,M = map(int,input().split())

q = deque()
q.append([N,0])
# 방문
visited = [0] * 100001
visited[N] = 1

# BFS
while q:
    # 현위치, 카운트
    now, cnt = q.popleft()
    # 도달하면 현위치 출력
    if now == M:
        print(cnt)
        break
    for i in [now-1,now+1,2*now]:
        # 범위를 설정해주지 않으면 런타임에러
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = 1
            q.append([i,cnt+1])