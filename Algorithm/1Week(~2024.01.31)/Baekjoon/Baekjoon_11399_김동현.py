import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

# 사람이 1명일 경우 계산할 필요가 없음
if len(lst) == 1:
    print(lst[0])
else:
    lst.sort()
    sum_min = lst[0]
    for i in range(1,len(lst)):
        sum_min = sum_min + sum(lst[:i+1]) # 했던 사람들 시간도 더하는 수식
    print(sum_min)

# 위 코드의 시간 복잡도는 O(N log N) 
# 이유: sort를 사용해서