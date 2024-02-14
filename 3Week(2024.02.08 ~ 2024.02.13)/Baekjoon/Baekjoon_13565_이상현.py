import sys
sys.setrecursionlimit(1000000)

# 백준 13565번 침투
# 이 문제는 격자가 주어지고 맨 윗줄의 격자에서 전류를 흘려보냈을 때
# 맨 밑줄까지 전달될 수 있는지를 판단하는 문제 (1에 막히지 않고 연결돼있는지 여부)

def dfs(row, col, temp):
    # 만약 범위를 벗어나거나 이미 방문한 혹은 전류가 흐르지 않는 격자라면 함수 종료
    if not (0 <= row < M and 0 <= col < N) or temp[row][col] != '0':
        return

    # 방문 처리
    temp[row][col] = '2'
    dfs(row + 1, col, temp)
    dfs(row - 1, col, temp)
    dfs(row, col + 1, temp)
    dfs(row, col - 1, temp)
    return

M, N = map(int, input().split())
list_ = [list(input()) for _ in range(M)]

# 맨 윗줄에서 전류를 흘려보냄
for col in range(N):
    dfs(0, col, list_)

# 하나라도 전류가 전달됬으면 'YES'를 출력, 그렇지 않으면 'NO'를 출력
print('YES' if any(list_[M - 1][col] == '2' for col in range(N)) else 'NO')

# 링크 : https://www.acmicpc.net/problem/13565