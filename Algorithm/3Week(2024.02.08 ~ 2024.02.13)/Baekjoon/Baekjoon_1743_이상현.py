import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

# 백준 1743번 음식물 피하기
# 1926번 문제와 유사한 문제, but 전역변수 사용
# 이 문제는 가장 큰 음식물의 크기를 구해야 함

def dfs(row, col, list_, visited):
    global cnt

    # 범위를 벗어나면 함수 종료
    if not (0 <= row < len(list_) and 0 <= col < len(list_[0])):
        return 0

    # 방문하지 않은 음식물이면 방문 처리 후 음식물 크기를 증가하고
    # 또다시 주변 칸에서 함수를 재귀적으로 호출
    if not visited[row][col] and list_[row][col] == '#':
        visited[row][col] = True
        cnt += 1

        dfs(row + 1, col, list_, visited)
        dfs(row - 1, col, list_, visited)
        dfs(row, col + 1, list_, visited)
        dfs(row, col - 1, list_, visited)
        return cnt

    return cnt

N, M, K = map(int,input().split())
list_ = [['.'] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 음식물의 좌표를 입력받아 리스트에 표시해줌
for _ in range(K):
    row, col = map(int, input().split())
    list_[row - 1][col - 1] = '#'

max_ = 0

for row in range(N):
    for col in range(M):
        cnt = 0
        temp = dfs(row, col, list_, visited)

        if temp > max_:
            max_ = temp

print(max_)

# 링크 : https://www.acmicpc.net/problem/1743