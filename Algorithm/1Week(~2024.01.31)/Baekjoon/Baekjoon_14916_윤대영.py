n = int(input())
two_coin, five_coin = 0, 0

while n  > 0:
    if n % 10 == 0: # n이 2, 5의 최소 공배수라면,
        five_coin += n // 5 # 5원 동전으로 모두 해결한다.
        n %= 5
    elif (n - 5) % 2 == 0: # n에서 5원 동전을 하나 쓰고 남은 값이 2원 동전으로 해결이 된다면, 
        five_coin += 1 # 5원 동전을 하나 사용한다.
        n -= 5
    else:
        two_coin += 1 # 위의 조건을 모두 만족하지 않는다면, 2원 동전 하나 사용한다.
        n -= 2

if n == 0:
    print(two_coin + five_coin)
else:
    print(-1)

# 출처 : https://www.acmicpc.net/problem/14916