import sys
input = sys.stdin.readline

def dfs(n,m):
    visited[n] = True
    # if n == m:                                                                           # sys를 사용한 완전 탐색 강제 종료
    #     print(count[end_node])               
    #     sys.exit()
    for i in graph[n]:
        if not visited[i]:
            count[i] = count[n] + 1
            dfs(i,m)

# 변수              
big_number = int(input())
start_node,end_node = map(int,input().split())                                                                    
N = int(input())
graph = [[] for i in range(big_number+1)]

# 방문 확인 밑 깊이 확인
visited = [False]*(big_number+1)
count = [0]*(big_number+1)

# 그래프 그리기
for _ in range(N):
    parent, son = map(int,input().split())
    graph[parent].append(son)
    graph[son].append(parent)

dfs(start_node,end_node)

# 함수 종료 후 결과 출력
print(count[end_node] if count[end_node] > 0 else -1)
# print(-1)                                                         # sys.exit에 걸리지 않은 것을 프린트


'''

간단한 백트래킹을 이용한 완전탐색 중 정답이 나왔을 경우 break(완전탐색인데 break 걸어서 모순일 수 있음)

import sys
input = sys.stdin.readline

def dfs(n,m):                                           # 지금 배운걸로는 한계라고 강사님 첨언
    global flag
    visited[n] = True
    print(visited)
    if n == m:
        flag = True
        return
    for i in graph[n]:
        if not visited[i]:
            count[i] = count[n] + 1
            dfs(i,m)
            if flag:
                return

# 변수
big_number = int(input())
start_node,end_node = map(int,input().split())
flag = False
N = int(input())
graph = [[] for i in range(big_number+1)]

# 방문 확인 밑 깊이 확인
visited = [False]*(big_number+1)
count = [0]*(big_number+1)

# 그래프 그리기
for _ in range(N):
    parent, son = map(int,input().split())
    graph[parent].append(son)
    graph[son].append(parent)

dfs(start_node,end_node)

# 함수 종료 후 결과 출력
print(count[end_node] if count[end_node] > 0 else -1)

# https://www.acmicpc.net/problem/2644

'''
# 이 코드의 시간 복잡도는 O(V+E)
    # DFS의 경우 시간 복잡도는 노드와 간선의 수에 비례함
    # 이때 V는 노드의 수, E는 간선의 수