import sys
sys.stdin = open("input.txt", "r")

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]  # dp생성
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if dp[i][j]>0 and lst[i][j]>0:  # 그 칸에 올수 있는 경로가 있고, 0이 아닌 경우
            k = lst[i][j]
            if j+k < N:  # 오른쪽 범위 이내인 경우
                dp[i][j+k] += dp[i][j]
            if i+k < N:  # 아래쪽 범위 이내인 경우
                dp[i+k][j] += dp[i][j]

print(dp[N-1][N-1])  # 젤 끝에 도달했을 떄 dp값

'''
시간복잡도 O(n**2)
https://www.acmicpc.net/problem/1890
'''