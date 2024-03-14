N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * N for _ in range(N)]
result[0][0] = 1

for row in range(N):
    for col in range(N):
        if not result[row][col]:
            continue

        if (row, col) == (N - 1, N - 1):
            break

        jump = list_[row][col]

        if 0 <= row + jump < N:
            result[row + jump][col] += result[row][col]

        if 0 <= col + jump < N:
            result[row][col + jump] += result[row][col]

print(result[N - 1][N - 1])