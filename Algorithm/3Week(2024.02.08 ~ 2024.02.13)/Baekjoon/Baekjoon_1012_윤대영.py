import sys

sys.setrecursionlimit(10 ** 8)

def dfs(pos, matrix, visited):
    n, m = len(matrix), len(matrix[0])
    cur_x, cur_y = pos
    visited[cur_x][cur_y] = 1
    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    for i in range(4):
        temp_x = cur_x + dx[i]
        temp_y = cur_y + dy[i]

        if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:  # 범위 벗어나면, continue로 방향 바꿈
            continue
        elif visited[temp_x][temp_y] == 0 and matrix[temp_x][temp_y] == 1:  # 방문 안한 곳이고, 배추가 있다면 dfs 호출
            dfs((temp_x, temp_y), matrix, visited)

    return True


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())  # 가로 m, 세로 n, 배추 위치 수 k
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    coordinate_lst = []
    ground_cnt = 0

    for _ in range(k):
        y, x = map(int, input().split())    # 가로(열) x, 세로(행) y
        matrix[x][y] = 1
        coordinate_lst.append((x, y))       # 배추 있는 좌표만 추가

    for pos in coordinate_lst:
        x, y = pos

        if visited[x][y] == 0:
            dfs(pos, matrix, visited)
            ground_cnt += 1

    print(ground_cnt)


# 시간복잡도: O(k * 4^k)
# 출처: https://www.acmicpc.net/problem/1012