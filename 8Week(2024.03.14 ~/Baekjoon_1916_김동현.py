import heapq,sys
input = sys.stdin.readline


def Dijkstra(start,end):
    quque = []
    heapq.heappush(quque,[0,start])
    min_list = [float('inf') for _ in range(N + 1)]
    while quque:
        sum_cash,start = heapq.heappop(quque)               # 우선순위 큐니까 순서 중요
        # 무조건 도착할 수 있으므로 리턴을 이곳에 해도 됨
        if start == end:
            return sum_cash

        for node in graph[start]:
            end_city,cash = node[1],node[0]
            if_cash = sum_cash + cash

            # if 문을 여기서 돌려줘야지 시간 초과가 나지 않음
            if min_list[end_city] > if_cash:
                min_list[end_city] = if_cash
                heapq.heappush(quque,[if_cash,end_city])


N,M = int(input()),int(input())
graph = [list() for _ in range(N+1)]
for _ in range(M):
    start_city,end_city,cash = map(int,input().split())
    graph[start_city].append([cash,end_city])
start,end = map(int,input().split())

print(Dijkstra(start,end))

# https://www.acmicpc.net/problem/1916
# 이코드의 시간 복잡도는 O(Nlog(N))
# 우선순위 큐연산이 while에서 이루어지기 때문에
# 한 번 틀렸는데 이유가 sys로 안받아서 시간 초과 남
# 이제 부터 함수 이름 Dijkstra로 고정하려함
