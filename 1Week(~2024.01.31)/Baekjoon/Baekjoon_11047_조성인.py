# 동전의 종류 수, 총 가치
N, K = map(int,input().split())

# 동전 종류 리스트
coin_list = []
for n in range(N):
    coin_list.append(int(input()))

# 동전 개수 카운트
count = 0
# 동전 종류를 크기 순대로 사용하기 위해 역순으로 사용
for coin in coin_list[::-1]:

    # 런타임 에러(마이너스 연산을 반복)
    # while K - coin >= 0:
    #     K -= coin
    #     count += 1

    # 몫과 나머지를 통해 한번에 연산
    while K - coin >= 0:
        count += K // coin
        K %= coin

        # 가치가 0이 되면 멈춰서 다음 K - coin을 하지 않음 
        if K == 0:
            break

print(count)