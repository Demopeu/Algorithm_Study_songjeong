def dfs(start, graph, visited):
    visited[start] = 1              # 1: 방문했다(바이러스에 감염됐다)
    
    for com in graph[start]:
        if visited[com] == 0:
            dfs(com, graph, visited)
    
    return visited

com_cnt = int(input())
connected_cnt = int(input())
network = [[] for _ in range(com_cnt + 1)]      # computer 연결 graph
connected = [0 for _ in range(com_cnt + 1)]     # 바이러스 전염 되었는지 확인(visited)

for _ in range(connected_cnt):
    start_com, end_com = map(int, input().split())
    network[start_com].append(end_com)
    network[end_com].append(start_com)          # 양방향으로 바이러스 전염 가능하기에 추가

connected = dfs(1, network, connected)          # 바이러스 전염된 computer list 할당

print(sum(connected) - 1)       # 감염된 computer에서 시작 computer 1은 뺴준다


# 시간복잡도: O(V + E)
# 출처: https://www.acmicpc.net/problem/2606