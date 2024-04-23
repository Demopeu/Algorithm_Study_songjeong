import heapq


def dijkstra():
    q = []
    heapq.heappush(q,[0,0,A])
    visited = [False]*(N+1)
    while q:
        max_suchi,sum_money,node = heapq.heappop(q)
        if node == B:
            if sum_money <= C:
                return max_suchi
            continue
        if not visited[node]:
            visited[node] = True
            for i in graph[node]:
                money,next_node = i[0],i[1]
                heapq.heappush(q,[max(max_suchi,money),sum_money+money,next_node])
    return -1


N,M,A,B,C = map(int,input().split())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    start,end,money = map(int,input().split())
    graph[start].append((money,end))
    graph[end].append((money,start))

print(dijkstra())

# https://www.acmicpc.net/problem/20168
# 우찌 풀엇노 걍 차력쇼함
# 이 코드의 시간복잡도는 O(V+E)log V
