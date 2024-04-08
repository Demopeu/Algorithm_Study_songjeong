import heapq
import sys
input = sys.stdin.readline


def bfs(start,sum_number):
    quque = []
    # 우선순위 힛큐니까 sum_number를 먼저 넣도록 합시다
    # 나랑 성인이 못찾음
    heapq.heappush(quque,[sum_number,start])
    min_list[start] = 0
    while quque:
        sum_number,start = heapq.heappop(quque)
        # 이미 거리 최소가 나오면 걸러
        if min_list[start] < sum_number:
            continue
        for node in graph[start]:
            cost = sum_number+node[1] # 0 도착지점 1 가중치
            # 만약 최소 거리가 갱신 된다면
            if min_list[node[0]] > cost:
                min_list[node[0]] = cost
                heapq.heappush(quque,[cost,node[0]])


V,E = map(int,input().split())
K = int(input())
graph = [list() for _ in range(V+1)]
# 최소 거리 리스트
min_list = [float('inf')] * (V + 1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

bfs(K,0)

for i in range(1,V+1):
    print(min_list[i] if min_list[i] != float('inf') else 'INF')


'''
시간 초과 코드

def bfs(start,sum_number):
    quque = []
    heapq.heappush(quque,[sum_number,start])
    min_list[start] = 0
    while quque:
        sum_number,start = heapq.heappop(quque)
        if min_list[start] < sum_number:
            continue
        min_list[start] = sum_number
        for node in graph[start]:
            cost = sum_number+node[1] # 0 도착지점 1 가중치
            if min_list[node[0]] > cost:

                heapq.heappush(quque,[cost,node[0]])



V,E = map(int,input().split())
K = int(input())
graph = [list() for _ in range(V+1)]
min_list = [float('inf')] * (V + 1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

bfs(K,0)

for i in range(1,V+1):
    print(min_list[i] if min_list[i] != float('inf') else 'INF')
    
바뀐 점이 먼저 갱신하고 다음 힛큐를 도냐 다음 힛큐에 도냐 차이인데 진짜 모름
'''

# https://www.acmicpc.net/problem/1753
# 이 코드의 시간 복잡도는  O(NlogN)
# BFS 탐색: O(VlogV + ElogV) = O((V+E)logV)