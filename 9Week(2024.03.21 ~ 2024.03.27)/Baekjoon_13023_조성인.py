# https://www.acmicpc.net/problem/13023

N,M = map(int,input().split())
# 그래프
graph = [[] for _ in range(N)]
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

# 초기 결과값 0으로 설정
result = 0

# 결국 재귀 사용
def DFS(now,cnt):
    global result
    # 4까지 가면 결과를 바꾸고 반환
    if cnt == 4:
        result = 1
        return
    visited[now] = 1
    for j in graph[now]:
        if not visited[j]:
            # while문으로는 이부분을 어떻게 하는지 모르겠음
            visited[j] = 1
            DFS(j, cnt + 1)
            visited[j] = 0

for i in range(N):
    # 방문
    visited = [0] * N
    # 함수
    DFS(i,0)
    # 종료
    if result:
        break

# 결과
print(result)

# while문 쓰려다 실패
# for i in range(N):
#     stack = [[i,0]]
#     visited = [0] * N
#     while stack:
#         now,cnt = stack.pop()
#         if cnt == 4:
#             result = 1
#             break
#         visited[now] = 1
#         for j in graph[now]:
#             if not visited[j]:
#                 stack.append([j,cnt+1])
#     if result:
#         break

