import sys
sys.stdin = open("input.txt", "r")

N = int(input())

dp = [0] * (N+1)  # dp[1] 초기값 설정

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:  # 2배수인 경우
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:  # 3배수인 경우
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])

'''
시간복잡도 O(n)
https://www.acmicpc.net/problem/1463
'''
