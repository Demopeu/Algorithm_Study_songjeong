from collections import deque


def bfs(start):
    queue = [[start, 0]]            # 레벨에 따른 숫자를 넣어준거
    queue = deque(queue)
    visited = [False]*(N+1)
    visited[start] = True
    parents = [0]*(N+1)             # 자식 칸에 부모가 들어갈 공간

    while queue:

        node = queue.popleft()

        for i in graph[node[0]]:

            if not visited[i]:

                parents[i] = node[0]        # 부모 기입
                visited[i] = True
                queue.append([i, node[1]+1])

    return parents


# 변수 설정
N = int(input())
graph = [[]for _ in range(N+1)]

# 그래프에 양쪽 기입
for _ in range(N-1):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

# 함수
answer = bfs(1)

# 출력문
for son in range(2, N+1):
    print(answer[son])





from collections import deque


def bfs(start):
    queue = [[start, 0]]            # 레벨에 따른 숫자를 넣어준거
    queue = deque(queue)
    visited = [False]*(N+1)
    visited[start] = True
    parents = [0]*(N+1)             # 자식 칸에 부모가 들어갈 공간

    while queue:

        node = queue.popleft()

        for i in graph[node[0]]:

            if not visited[i]:

                parents[i] = node[0]        # 부모 기입
                visited[i] = True
                queue.append([i, node[1]+1])

    return parents


# 변수 설정
N = int(input())
graph = [[]for _ in range(N+1)]

# 그래프에 양쪽 기입
for _ in range(N-1):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)

# 함수
answer = bfs(1)

# 출력문
for son in range(2, N+1):
    print(answer[son])


# https://www.acmicpc.net/problem/11725
# 이 코드의 시간 복잡도는 O(N)
    # 애초에 전체 슥슥 둘러보면서 내려가서 O(V+E)임
    # V가 N이고 E가 N으로 수렴해도 O(2N)임
    # 따라서 O(N)


