# https://www.acmicpc.net/problem/2156

N = int(input())
wine = [int(input()) for _ in range(N)]

# dp에는 그 잔까지의 최대 양을 저장
dp = [0] * N

# 3보다 작으면 그냥 합을 출력
if N < 3:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    # 3가지 경우의 수 : 1,2 or 1,3 or 2,3
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

    # 3 이후에는 위의 세 경우의 수에 그 경우 이전의 최댓값을 더해 최댓값을 구함
    for i in range(3,N):
        dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])

    print(max(dp))