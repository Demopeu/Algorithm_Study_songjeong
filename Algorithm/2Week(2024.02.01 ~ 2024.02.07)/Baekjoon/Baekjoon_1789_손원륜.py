# 서로 다른 N개의 자연수의 합 S
# S가 주어질 때, N의 최대값은

S = int(input())

cur = 0                     # 초기값
count = 0

while cur <= S:             # 현재수 cur이 S보다 작거나 같을때 반복
    count = count + 1
    cur = cur + count
    if cur <= S:
        continue
    else:                   # cur이 S보다 커지면 break
        break

print(count - 1)            # 한 번 더 카운트 된 것 이므로 -1 