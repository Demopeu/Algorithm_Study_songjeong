# 백준 14940번 쉬운 최단거리

from collections import deque

def bfs(start, graph):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[0] * m for _ in range(n)]
    # 목표 지점의 경우 visited에 '0'으로 저장한 이유는
    # 방문여부 + 목표지점부터의 거리를 한꺼번에 나타내기 위함
    visited[start[0]][start[1]] = '0'

    while q:
        # row, col은 현재위치, depth는 목표지점까지의 거리
        row, col, depth = q.popleft()

        for i in range(4):
            nrow, ncol = row + drow[i], col + dcol[i]

            # 지도의 범위를 벗어나거나 이미 방문했거나 갈 수 없는 곳이라면 탐색하지 않음
            if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and graph[nrow][ncol]:
                q.append((nrow, ncol, depth + 1))
                visited[nrow][ncol] = depth + 1

    return visited

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
start = -1, -1
drow, dcol = [1, 0, -1, 0], [0, -1, 0, 1]

# 입력받은 지도를 순회하며 목표 지점을 찾고 찾으면 반복문 종료
for row in range(n):
    for col in range(m):
        if graph[row][col] == 2:
            start = row, col
            break

    if start != (-1, -1):
        break

result = bfs(start, graph)

# 갈 수 있는 땅이지만 방문하지 않은 곳이 있다면 -1로 변경
for row in range(n):
    for col in range(m):
        if result[row][col] == 0 and graph[row][col] == 1:
            result[row][col] = -1

[print(*row) for row in result]

# 문제링크 : https://www.acmicpc.net/problem/14940
# 시간복잡도 : O(n * m)
# 39736 KB, 516 ms Python 3
# 121644 KB, 264 ms PyPy 3