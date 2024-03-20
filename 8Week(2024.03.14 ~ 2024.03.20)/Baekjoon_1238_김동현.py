import sys,heapq
input = sys.stdin.readline

def go_Dijkstra(start):
    quque = []
    heapq.heappush(quque,[0,start])
    while quque:
        sum_number,start = heapq.heappop(quque)
        if start == X:
            return sum_number
        for node in graph[start]:
            T,end = node[0],node[1]
            if go_min_list[end]>sum_number+T:
                go_min_list[end] = sum_number+T
                heapq.heappush(quque,[sum_number+T,end])


def back_Dijkstra(X):
    quque = []
    heapq.heappush(quque,[0,X])
    while quque:
        sum_number,start = heapq.heappop(quque)
        for node in graph[start]:
            T,end = node[0],node[1]
            if back_min_list[end] > T+sum_number:
                back_min_list[end] = T + sum_number
                heapq.heappush(quque,[sum_number+T,end])


N,M,X = map(int,input().split())
graph = [list() for _ in range(N+1)]
# 최단 거리 리스트
gogo_min_list = [float('inf') for _ in range(N+1)]
back_min_list = [float('inf') for _ in range(N+1)]
for _ in range(M):
    start,end,T = map(int,input().split())
    graph[start].append([T,end])

# 자기 도시에서 X까지 갈때 거리 구하기
for i in range(1,N+1):
    # 1회용 최저 거리 계산 리스트(나누는 이유는 i++ 마다 계속 갱신되기 때문에)
    go_min_list = [float('inf') for _ in range(N + 1)]
    # 진짜 최저 거리 계산 리스트
    gogo_min_list[i] =go_Dijkstra(i)

# X에서 자기도시까지 갈때 거리 구하기
back_Dijkstra(X)
answer = [i+j for i,j in zip(gogo_min_list[1:],back_min_list[1:])]
print(max(answer))

# https://www.acmicpc.net/problem/1238
# 이 코드의 시간 복잡도는 O(N^2*(logN))
# 걍 해봤는데 이게 성공해서 되게 당황스럽다
# 시간 제한 1초인데 O(N^2*(logN)) 돌아가는게 이상함
# 찾아봣는데 다들 이렇게 풀어놨음
