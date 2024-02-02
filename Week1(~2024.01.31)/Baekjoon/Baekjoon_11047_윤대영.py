n, k = map(int, input().split())
coin_lst = []
coin_cnt = 0

for _ in range(n):
    coin_lst.append(int(input())) # 동전 리스트에 동전 입력 받기

for coin in coin_lst[::-1]: # 큰 동전부터 반복문 돌면서 먼저 사용하기
    if k <= 0:
        break
    if k >= coin:
        coin_cnt += k // coin
        k %= coin
print(coin_cnt)

# 출처 : https://www.acmicpc.net/problem/11047