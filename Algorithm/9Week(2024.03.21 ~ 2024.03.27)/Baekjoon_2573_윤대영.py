import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < m and visited[tx][ty] == 0 and icebergs[tx][ty] > 0:
                q.append((tx, ty))
                visited[tx][ty] = 1


def rower_icebergs():       # 빙산 높이 낮추는 함수
    new_icebergs = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if icebergs[i][j] > 0:
                water = 0                                       # 동서남북 바닷물 수
                for k in range(4):
                    if icebergs[i + dx[k]][j + dy[k]] <= 0:     # 0 이하면 바닷물 취급
                        water += 1
                new_icebergs[i][j] = icebergs[i][j] - water     # 직접 icebergs 건들면 중간에 0 이하 생기면서 빙산 전부 한번에 1 줄어드지 않음
    return new_icebergs


def check_icebergs():
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if icebergs[i][j] > 0:
                return False                # 빙산 하나라도 남아있다면 return False
    return True

# main 함수
n, m = map(int, input().split())    # n: 행의 수, m: 열의 수
icebergs = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False
result = 0
year = 0

while True:
    cnt = 0                         # bfs 함수 호출 횟수(빙산 덩어리 개수)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            if icebergs[r][c] > 0 and visited[r][c] == 0:
                bfs((r, c))
                cnt += 1
                if cnt > 1:
                    flag = True
                    result = year
                    break
        if flag:
            break
    if flag:
        break
    icebergs = rower_icebergs()     # 처음부터 분리된 경우 파악 위해 위치 맨 아래로 변경
    year += 1
    if check_icebergs():
        result = 0
        break

print(result)


# 시간복잡도: O(n * m)
# 출처: https://www.acmicpc.net/problem/2573