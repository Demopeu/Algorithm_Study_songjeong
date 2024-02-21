from collections import deque
# def bfs(start):
#     queue = [[start,1]]
#     queue = deque(queue)
#     while queue:
#
#         node = queue.popleft()
#
#         if node[0] > M:
#             continue
#         if node[0] == M:
#             return node[1]
#
#         queue.append([node[0]*2,node[1]+1])
#         queue.append([int(str(node[0])+str(1)),node[1]+1])
#     return -1'


def dfs(start):
    queue = [[start, 1]]                # 1부터 숫자 셈

    while queue:
        node = queue.pop()

        if node[0] > M:                 # 더 크면 걍 거름
            continue
        if node[0] == M:
            return node[1]

        queue.append([node[0]*2,node[1]+1])
        queue.append([int(str(node[0])+str(1)),node[1]+1])

    return -1


N,M = map(int,input().split())
print(dfs(N))

# 이 코드의 시간 복잡도는 O(M)
    # M을 넘지 않는 자연수이기 때문

# 분명 BFS에서 문제 찾은건데 런타임에러남;;
# https://www.acmicpc.net/problem/16953