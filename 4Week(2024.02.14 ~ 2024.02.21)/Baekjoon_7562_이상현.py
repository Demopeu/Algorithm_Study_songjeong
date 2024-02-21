# 백준 7562번 나이트의 이동

from collections import deque

# 나이트가 최소 몇 번 움직여야 시작 칸에서 목표 칸으로 
# 이동할 수 있는지 구하는 문제

# 나이트가 이동할 수 있는 경우를 저장
drow = [-2, -1, 1, 2, 2, 1, -1, -2]
dcol = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(start):
    q = deque()
    q.append((start[0], start[1], 0))
    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1

    while q:
        # row, col은 현재 칸의 위치, cnt는 현재까지의 이동 횟수
        row, col, cnt = q.popleft()

        # 목표에 도달했다면 반복문 종료
        if (row, col) == end:
            break

        for i in range(8):
            nrow, ncol = row + drow[i], col + dcol[i]

            # 나이트가 이동할 수 있는 칸 중 방문하지 않은 곳이 있다면
            # 방문처리 후 cnt를 1 증가시키고 탐색
            if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol]:
                q.append((nrow, ncol, cnt + 1))
                visited[nrow][ncol] = 1

    # 이동횟수를 반환
    return cnt

T = int(input())

for tc in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(start))

# 문제링크 : https://www.acmicpc.net/problem/7562
# 시간복잡도 : O(T * N^2)
# 34088 KB, 1344 ms Python 3
# 132028 KB, 332 ms PyPy 3