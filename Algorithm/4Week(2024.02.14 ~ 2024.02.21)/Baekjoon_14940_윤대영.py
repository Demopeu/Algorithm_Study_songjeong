import sys
from collections import deque

input = sys.stdin.readline  # 시간 초과 문제로 input에서 변경

def bfs(x, y, matrix):
    visit = [[0 for _ in range(m)] for _ in range(n)]     # bfs 호출 전 visited 선언 및 초기화

    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    v_cnt = 0

    while q:                # q가 빌 때까지 반복
        v_cnt += 1          # 최단 거리
        temp = deque()
        while q:            # 한 depth가 빌 때까지 반복하며, 다음 depth들만 append
            x, y = q.popleft()      # 시간 초과 문제로 for문 대신 q.popleft() 사용
            if visit[x][y] == 1 and matrix[x][y] == 2:
                    return v_cnt - 1    # 첫 시작할 때부터 1을 추가하고 시작해서 -1만큼 보정 
            else:
                for i in range(4):
                    temp_x = x + dx[i]
                    temp_y = y + dy[i]
                    if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:
                        continue
                    if visit[temp_x][temp_y] == 1 or matrix[temp_x][temp_y] == 0:
                        continue
                    temp.append((temp_x, temp_y))   # temp queue에 임시로 다음 depth들만 append
                    visit[temp_x][temp_y] = 1       # 시간 초과 문제로 append와 동시에 visit 체크
        q = temp        # q에 temp 할당함으로써, 큰 while문 멈추지 않고 반복됨
    return -1


n, m = map(int, list(input().split()))    # n: 세로, m: 가로
directions = [list(map(int, list(input().split())))for _ in range(n)]
distances = [[0 for _ in range(m)] for _ in range(n)]   # 최단 거리 기록할 2차원 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for r in range(n):
    for c in range(m):
        if directions[r][c] == 1:
            distances[r][c] = bfs(r, c, directions)

for row in distances:
    print(*row)


# 시간복잡도: O(NM)
# 출처: https://www.acmicpc.net/problem/14940