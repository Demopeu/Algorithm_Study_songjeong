import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited[start] = 1
    while q:
        pos, cnt = q.popleft()
        if pos == 100:
            return cnt
        for dice in [1, 2, 3, 4, 5, 6]:
            new_pos = pos + dice
            if 0 < new_pos <= 100 and visited[new_pos] == 0:
                if new_pos in ladders.keys():       # 사다리 도착
                    new_pos = ladders[new_pos]
                    q.append((new_pos, cnt + 1))
                    visited[new_pos] = 1
                elif new_pos in snakes.keys():      # 뱀 도착
                    new_pos = snakes[new_pos]
                    q.append((new_pos, cnt + 1))
                    visited[new_pos] = 1
                else:                               # 일반 칸 도착
                    q.append((new_pos, cnt + 1))
                    visited[new_pos] = 1


n, m = map(int, input().split())    # n: 사다리의 수, m: 뱀의 수
game_map = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
ladders = {}
snakes = {}

for _ in range(n):
    x, y = map(int, input().split())    # x번 칸 -> y번 칸
    ladders[x] = y

for _ in range(m):
    u, v = map(int, input().split())    # u번 칸 -> v번 칸
    snakes[u] = v

print(bfs(1))


# 시간복잡도: O(1)
# 출처: https://www.acmicpc.net/problem/16928