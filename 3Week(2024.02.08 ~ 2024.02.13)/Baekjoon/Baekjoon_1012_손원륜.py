import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

MAX_COL = 50 + 10
MAX_ROW = 50 + 10

dir_r = [1, -1, 0, 0]
dir_c = [0, 0, 1, -1]

def dfs(row, col):
    graph[row][col] = False
    for dir_idx in range(4):
        new_row = row + dir_r[dir_idx]
        new_col = col + dir_c[dir_idx]
        if graph[new_row][new_col]:
            dfs(new_row, new_col)

# 0. 입력 및 초기화
test_cases = int(input())  # 테스트 케이스의 개수 입력
for _ in range(test_cases):
    cols, rows, islands = map(int, input().split())  # 열의 개수, 행의 개수, 섬의 개수 입력
    graph = [[False] * MAX_COL for _ in range(MAX_ROW)]  # 그래프 초기화

    # 1. 그래프 정보 입력
    for _ in range(islands):
        col, row = map(int, input().split())  # 섬의 좌표 입력
        graph[row + 1][col + 1] = True  # 섬의 위치 표시

    # 2. 방문하지 않은 지점부터 DFS 돌기
    answer = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if graph[i][j]:  # 방문하지 않은 섬인 경우
                dfs(i, j)  # DFS 탐색
                answer += 1  # 섬의 개수 증가
    print(answer)  # 결과 출력

'''
시간 복잡도는 O(NM)
https://www.acmicpc.net/problem/1012
'''

