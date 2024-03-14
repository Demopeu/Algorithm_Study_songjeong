# https://www.acmicpc.net/problem/1890

# 원래는 queue를 사용한 bfs로 풀려고 했으나 메모리 초과

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
# 해당 위치를 방문하는 경로를 카운트
roots = [[0]*N for _ in range(N)]
roots[0][0] = 1

# 2차원 배열을 순회하면서 지난 횟수를 추가(우하향으로 진행하기 때문에 가능)
for i in range(N):
    for j in range(N):
        # 0이면 연산할 필요가 없음
        if matrix[i][j] != 0:
            # 범위 안일때
            if i + matrix[i][j] < N:
                # 여기까지 도달하는 경로개수 추가
                roots[i + matrix[i][j]][j] += roots[i][j]
            # 범위 안일때
            if j + matrix[i][j] < N:
                # 여기까지 도달하는 경로개수 추가
                roots[i][j + matrix[i][j]] += roots[i][j]
 
# 도착지의 경로 개수 출력                
print(roots[N-1][N-1])