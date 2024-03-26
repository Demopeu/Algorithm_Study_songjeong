from collections import deque
import sys
input = sys.stdin.readline


def find(count,start):
    queue = deque([(count,start)])
    visited = [False]*101
    visited[start] = True

    while queue:
        count,node = queue.popleft()

        if node == 100:
            return count

        for l in range(1,7):
            new_node = node + l

            if new_node <=100:
                if visited[new_node]:
                    continue

                visited[new_node] = True

                if ladder[new_node]:
                    queue.append((count+1,ladder[new_node][0]))
                elif snake[new_node]:
                    queue.append((count + 1, snake[new_node][0]))
                else:
                    queue.append((count+1,new_node))
    return 100

N,M = map(int,input().split())
ladder = [[]for _ in range(101)]
snake = [[]for _ in range(101)]
for _ in range(N):
    x,y = map(int,input().split())
    ladder[x].append(y)
for _ in range(M):
    u,v = map(int,input().split())
    snake[u].append(v)

print(find(0,1))

# https://www.acmicpc.net/problem/16928
# 이 코드의 시간 복잡도는 O(1)
# 최악의 경우 O(100)

# 간단한 문제였는데, 처음에 왜 visited 쓰는 지 몰랐음
# 1초에 512mb이고 N이 100개여서 ㄱㅊ다고 생각
# 처음에 heapq로 구현하고 visited 안쓰다가 메모리 초과남
# 그래서 그냥 bfs 얌전히 썻읍니다
# 지금 돌이켜 보면 visited 순서가 마음에 안듬
# 효율 좋게 바꿀 수 있을 거 같음
