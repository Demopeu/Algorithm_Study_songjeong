import sys
input = sys.stdin.readline


N = int(input())
bag = 0

# 5의 약수가 아닐 경우 3키로 봉지 사용
while N>=0:
    if N % 5 == 0:
        bag += N//5
        print(bag)
        break
    N -= 3
    bag += 1
# break 안될 경우 print(-1)
else:
    print(-1)



# 위 코드의 시간 복잡도는 O(n)