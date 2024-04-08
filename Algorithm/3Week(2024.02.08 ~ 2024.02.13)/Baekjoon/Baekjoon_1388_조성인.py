# https://www.acmicpc.net/problem/1388

# 시간복잡도 : O(N * M)

N, M = map(int,input().split())
# 바닥
floor = [list(input()) for _ in range(N)]

# 판자 개수
count = 0
for i in range(N):
    for j in range(M):
        # 가로일 경우
        if floor[i][j] == '-':
            n = 0
            # 판자의 개수 +1
            count += 1
            # -일 경우 가로로 -를 판자 번호로 바꿔줌
            while j+n < M and floor[i][j+n] == '-':
                floor[i][j+n] = count
                n += 1
        # 세로일 경우
        elif floor[i][j] == '|':
            n = 0
            # 판자의 개수 +1
            count += 1
            # |일 경우 세로로 |를 판자 번호로 바꿔줌
            while i+n < N and floor[i+n][j] == '|':
                floor[i+n][j] = count
                n += 1
        # 숫자일 경우(이미 카운트된 바닥이므로 skip)
        else:
            continue

print(count)