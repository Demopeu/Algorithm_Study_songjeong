import sys
sys.setrecursionlimit(250000)
# sys.stdin = open('input.txt')

# 백준 1926번 그림
# 이 문제는 그림의 개수 (나눠져 있는 영역의 개수)와
# 그 그림들 중 가장 넓은 그림의 넓이를 구하는 문제

def dfs(row, col, graph, visited):
    # 범위를 벗어나면 함수 종료
    if not (0 <= row < len(graph) and 0 <= col < len(graph[0])):
        return 0

    # 방문하지 않았고, 색칠이 된 부분이면 방문처리 후 재귀함수 호출
    if not visited[row][col] and graph[row][col]:
        visited[row][col] = True
        temp = 1

        temp += dfs(row + 1, col, graph, visited)
        temp += dfs(row - 1, col, graph, visited)
        temp += dfs(row, col + 1, graph, visited)
        temp += dfs(row, col - 1, graph, visited)
        return temp

    return 0


n, m = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
max_ = 0
area_num = 0

for row in range(n):
    for col in range(m):
        area = dfs(row, col, list_, visited)

        if area > 0:
            area_num += 1
            max_ = max(area, max_)

print(area_num)
print(max_)

# 링크 : https://www.acmicpc.net/problem/1926