import sys
from collections import deque

input = sys.stdin.readline


def bfs(start, high):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n and visited[tx][ty] == 0 and heights[tx][ty] > high:
                q.append((tx, ty))
                visited[tx][ty] = 1


n = int(input())    # n: 행과 열의 수
heights = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
safety = 0
max_safety = -sys.maxsize

for h in range(101):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    safety = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 0 and heights[r][c] > h:
                bfs((r, c), h)
                safety += 1
    if safety > max_safety:
        max_safety = safety

print(max_safety)


# 시간복잡도: O(n^2)
# 출처: https://www.acmicpc.net/problem/2468