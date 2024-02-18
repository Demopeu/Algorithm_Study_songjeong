def dfs(x, y, colors):

    stack = [(x,y)]
    people = 0
    while stack:

        node = stack.pop()
        if not visited[node[0]][node[1]] and matrix[node[0]][node[1]] == colors:
            people += 1
            visited[node[0]][node[1]] = True

            for l in range(4):

                new_i = node[0] + dx[l]
                new_j = node[1] + dy[l]

                if 0<= new_i < M and 0 <= new_j < N:

                    if not visited[new_i][new_j] and matrix[new_i][new_j] == colors:
                        stack.append((new_i, new_j))

    return people*people


# 변수 설정
N, M = map(int, input().split())
matrix = [input() for _ in range(M)]
visited = [[False]*N for _ in range(M)]
W_count = 0
B_count = 0

# 좌표계 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 함수 실행
for i in range(M):
    for j in range(N):

        # 팀 구별
        color = matrix[i][j]

        # 방문 하지 않았을 경우
        if not visited[i][j]:
            count = dfs(i, j, color)

            if color == 'W':
                W_count += count
            else:
                B_count += count

# 결과문
print(f'{W_count} {B_count}')

# https://www.acmicpc.net/problem/1303
# 다들 재귀로 풀길래 재귀는 생략
# 이 코드의 복잡도는 O(N*M)
