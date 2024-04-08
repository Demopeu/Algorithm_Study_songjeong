T = int(input())

# 아래 now에 들어간 방향
# go = ['r','d','l','u']

for test_case in range(1,T+1):
    # 사과 개수
    N = int(input())
    # 맵
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 각 사과의 위치 기록
    apples = [0] * 11
    # 0번째 사과는 시작점으로 사용
    apples[0] = [0,0]
    # 현재 방향(시작은 오른쪽)
    now = 0
    # 방향 전환 횟수 카운트
    count = 0

    # 일단 사과들 위치 기록
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                apples[matrix[i][j]] = [i,j]

    for i in range(10):
        # 다음 사과가 있을때(좌표값이 들어있을 경우)
        if apples[i+1]:
            # 다음 사과의 위치와 현재 방향별로 돌아야 되는 횟수와 결과 방향이 정해져 있음
            # 우하단
            if apples[i][0] < apples[i+1][0] and apples[i][1] < apples[i+1][1]:
                if now == 0:
                    count += 1
                    now = 1
                elif now == 1:
                    count += 3
                    now = 0
                elif now == 2:
                    count += 3
                    now = 1
                else:
                    count += 2
                    now = 1
            # 좌하단
            elif apples[i][0] < apples[i+1][0] and apples[i][1] > apples[i+1][1]:
                if now == 0:
                    count += 2
                    now = 2
                elif now == 1:
                    count += 1
                    now = 2
                elif now == 2:
                    count += 3
                    now = 1
                else:
                    count += 3
                    now = 2
            # 우상단
            elif apples[i][0] > apples[i+1][0] and apples[i][1] < apples[i+1][1]:
                if now == 0:
                    count += 3
                    now = 3
                elif now == 1:
                    count += 3
                    now = 0
                elif now == 2:
                    count += 2
                    now = 0
                else:
                    count += 1
                    now = 0
            # 좌상단
            elif apples[i][0] > apples[i+1][0] and apples[i][1] > apples[i+1][1]:
                if now == 0:
                    count += 3
                    now = 3
                elif now == 1:
                    count += 2
                    now = 3
                elif now == 2:
                    count += 1
                    now = 3
                else:
                    count += 3
                    now = 2
            
    print(f'#{test_case} {count}')