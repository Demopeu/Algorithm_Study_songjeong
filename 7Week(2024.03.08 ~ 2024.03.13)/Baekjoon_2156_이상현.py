n = int(input())
list_ = [int(input()) for _ in range(n)]
dp = [list_[0]] + [0] * (n - 1)

if n > 1:
    dp[1] = list_[1] + list_[0]

if n > 2:
    dp[2] = max(list_[2] + list_[1], list_[1] + list_[0], list_[2] + list_[0])

for i in range(3, n):
    dp[i] = max(list_[i] + list_[i - 1] + dp[i - 3], list_[i] + dp[i - 2], dp[i - 1])

print(max(dp))