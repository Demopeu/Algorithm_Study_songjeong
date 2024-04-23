N,d,k,c = map(int,input().split())
lst = list(int(input()) for _ in range(N))
max_sushi = 0
for i in range(N):
    if i + k <= N:
        sushi = set(lst[i:i+k])
    else:
        sushi=set(lst[i:])|set(lst[:((i+k)%N)])
    sushi.add(c)
    max_sushi = max(max_sushi,len(sushi))
print(max_sushi)

# https://www.acmicpc.net/problem/2531
# 슬라이싱 윈도우 쓰라는데 걍 set 완탐 돌림