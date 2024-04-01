# https://www.acmicpc.net/problem/16928

from collections import deque

N,M = map(int,input().split())

# 사다리, 뱀
road = {}
for i in range(N):
    A,B = map(int,input().split())
    road[A] = B
for i in range(M):
    A,B = map(int,input().split())
    road[A] = B

# 방문처리
visited = [0] * 101

q = deque()
# 굴린횟수, 말의 위치(1부터 출발)
q.append([0,1])
while q:
    roll,now = q.popleft()
    # 100에 도달하면 종료
    if now == 100:
        break
    # 주사위로 나올 수 있는 수 1~6
    for i in range(1,7):
        # 100보다 커지면 더 돌릴 필요 없음
        if now+i > 100:
            break
        # 사다리 또는 뱀에 도착하면 + 미방문 시 이동
        if now+i in road and not visited[now+i]:
            visited[road[now+i]] = roll+1
            q.append([roll+1,road[now+i]])
        # 미방문 시 이동
        elif not visited[now+i]:
            visited[now+i] = roll+1
            q.append([roll+1,now+i])

print(visited[100])