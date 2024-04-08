# https://www.acmicpc.net/problem/1932

N = int(input())
# 정수삼각형(단, 좌우를 0으로 감싸서)
triangle = [[0] + list(map(int,input().split())) + [0] for _ in range(N)]

# 그냥 단순하게 위의 두 값중 큰 값을 아래에 더해줌
for i in range(1,N):
    for j in range(i+3):
        if 0 < j < i+2:
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

# 그렇게 나온 삼각형의 마지막 줄의 최대값 출력
print(max(triangle[-1]))