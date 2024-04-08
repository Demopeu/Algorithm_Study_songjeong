import sys

sys.setrecursionlimit(10 ** 6)

def dfs(x, y, matrix, visited):
    visited[x][y] = 1

    for i in range(8):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if temp_x < 0 or temp_x >= h or temp_y < 0 or temp_y >= w or matrix[temp_x][temp_y] == 0:
            continue
        if visited[temp_x][temp_y] == 0 and matrix[temp_x][temp_y] == 1:
            dfs(temp_x, temp_y, matrix, visited)
    return visited


while True:
    w, h = map(int, input().split())    # 너비 w, 높이 h
    matrix = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]    # 상하좌우, 대각선 4방향
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    island_cnt = 0

    if w == 0 and h == 0:
        break

    for r in range(h):
        for c in range(w):
            if matrix[r][c] == 1 and visited[r][c] == 0:
                dfs(r, c, matrix, visited)
                island_cnt += 1
    print(island_cnt)


# 시간복잡도: O(NM)
# 출처: https://www.acmicpc.net/problem/4963