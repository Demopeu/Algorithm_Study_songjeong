# https://www.acmicpc.net/problem/1238

import heapq

# 마을 수, 도로 수, 기준점
N,M,X = map(int,input().split())
# 그래프 사용
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S,E,T = map(int,input().split())
    graph[S].append([E,T])

# 갔다가 다시 돌아오는 왕복 문제
# 각 마을마다 최단 거리를 다 구해주기

# 최단거리 리스트의 리스트
distance_lists = []

# 모든 마을마다 최단거리 작성
for i in range(N+1):

    # 마을별 최단 거리 리스트
    # 0번(존재하지 않는 마을)이랑 현 위치는 0
    times = [float('inf')] * (N+1)
    times[0] = times[i] = 0

    hq = [(0,i)]

    while hq:
        # 걸린 시간, 마을
        time_sum, city = heapq.heappop(hq)
        # 마을의 도로를 순회
        for end,time in graph[city]:
            # 최단시간 갱신 및 큐에 추가
            if times[end] > time_sum + time:
                times[end] = time_sum + time
                heapq.heappush(hq,(time_sum + time, end))
    
    # 반복문 종료 후 최단 거리 리스트를 리스트에 넣음
    distance_lists.append(times[:])

# 최종 결과
result = []
for i in range(1,N+1):
    # i번 마을에 대해 X번으로 가는 최단거리 + X번에서 오는 최단거리를 추가
    result.append(distance_lists[i][X] + distance_lists[X][i])

# 제일 오래 걸리는 시간을 출력
print(max(result))