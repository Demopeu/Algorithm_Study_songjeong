# https://www.acmicpc.net/problem/1012

# 시간 복잡도 O(N * M + K)

T = int(input())

dx = [0,1,0,-1]
dy = [-1,0,1,0]

for test_case in range(1,T+1):
    M,N,K = map(int, input().split())
    # 배추 좌표
    cabbages = [list(map(int,input().split())) for _ in range(K)]
    # 2차원 밭
    matrix = [[0]*M for _ in range(N)]
    
    # 배추 심기
    for i in range(N):
        for j in range(M):
            if [j, i] in cabbages:
                matrix[i][j] = 1
    
    # 필요한 벌레 수
    count = 0

    for i in range(N):
        for j in range(M):
            # DFS용 스택
            stack = []
            # 배추 발견 했을 때 벌레 1추가 하고 반복용 스택 사용
            if matrix[i][j] == 1:
                count += 1
                stack.append([j,i])
            while stack:
                [x,y] = stack.pop()
                # 확인한 자리는 빈칸으로 바꿈
                matrix[y][x] = 0
                # 4방향
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    # 밭 안 빠져 나가고 배추가 있으면
                    if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1:
                        # 스택에 추가
                        stack.append([nx,ny])

    print(count)