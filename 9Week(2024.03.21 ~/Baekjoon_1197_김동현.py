import heapq
def prim(start):
    queue = [[0,start]]
    visited = list(False for _ in range(V+1))
    sum_number = 0

    while queue:
        number,node = heapq.heappop(queue)
        # 이미 큐에 드가 잇는 애들 중에 거르는 구문
        if visited[node]:
            continue
        visited[node] = True
        sum_number += number
        for w,e in graph[node]:
            if not visited[e]:
                heapq.heappush(queue,[w,e])
    return sum_number

V,E = map(int,input().split())
graph = list(list()for _ in range(V+1))
for _ in range(E):
    s,e,w = map(int,input().split())
    # 프림일 경우, 꼭 합시다
    graph[s].append([w,e])
    graph[e].append([w,s])
print(prim(1))

# https://www.acmicpc.net/problem/1197
# 이 코드의 시간 복잡도는 O(ElogV)
# 각 노드에서 모든 간선을 확인해야 하므로 O(E)
# 우선순위 큐를 이용하므로 O(logV)