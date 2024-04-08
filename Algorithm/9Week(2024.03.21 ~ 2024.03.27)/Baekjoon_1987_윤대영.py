import sys

input = sys.stdin.readline


def dfs(x, y, move):
    global max_move
    alpha_check[ord(board[x][y]) - 65] = 1

    if move > max_move:
        max_move = move
    if move > r * c or move > 26:   # 알파벳 수 초과거나, board 칸수 초과면 return
        return
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < r and 0 <= ty < c and alpha_check[ord(board[tx][ty]) - 65] == 0:
            alpha_check[ord(board[tx][ty]) - 65] = 1    # 모든 경우의 수 탐색 위해 방문 처리 및 DFS 호출 후 방문 미처리로 변경
            dfs(tx, ty, move + 1)
            alpha_check[ord(board[tx][ty]) - 65] = 0


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
alpha_check = [0 for _ in range(26)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_move = -sys.maxsize

dfs(0, 0, 1)
print(max_move)


# 시간복잡도: O(V + E)
# 출처: https://www.acmicpc.net/problem/1987