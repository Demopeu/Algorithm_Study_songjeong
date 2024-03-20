# https://www.acmicpc.net/problem/1916

# 우선순위 큐 사용
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 그래프 사용
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S,E,C = map(int,input().split())
    graph[S].append((E,C))

# 출발점, 도착점
A,B = map(int,input().split())

# 최소 비용 리스트
cities = [float('inf')] * (N+1)
cities[A] = 0

# 우선순위 큐
hq = [(0,A)]

while hq:
    # 현재 비용, 도시
    cost,current_city = heapq.heappop(hq)
    # 목적지에 도착했으면 반복 종료
    if current_city == B:
        break
    # 현재 도시와 연결된 노선을 순회
    for end,current_cost in graph[current_city]:
        # 목적지의 비용 갱신하면서 hq에 도시 추가
        if cities[end] > cities[current_city] + current_cost:
            cities[end] = cities[current_city] + current_cost
            heapq.heappush(hq, (cities[end],end))

print(cities[B])

# 시간초과(우선순위 큐를 사용하지 않음 - O(NM)
# N = int(input())
# M = int(input())
# buses = [list(map(int,input().split())) for _ in range(M)]
# A,B = map(int,input().split())
#
# cities = [float('inf')] * (N+1)
# cities[A] = 0
#
# for i in range(N):
#     for j in range(M):
#         if buses[j][0] == i+1 and cities[buses[j][1]] > cities[buses[j][0]]+buses[j][2]:
#             cities[buses[j][1]] = cities[buses[j][0]]+buses[j][2]
#
# print(cities[B])