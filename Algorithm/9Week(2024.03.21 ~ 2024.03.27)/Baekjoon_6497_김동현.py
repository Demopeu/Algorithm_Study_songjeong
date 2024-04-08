# 시간 초과 나서 sys로 받음
import sys
input = sys.stdin.readline

# 엄마 찾기
def find_set(x):
    # if parents[x] == x:
    #     return x
    # parents[x] = find_set(parents[x])
    while parents[x] != x:
        x = parents[x]
    return x


# 엄마 합치기(숫자 작은 게 승자)
def union_set(x,y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x<y:
        parents[y] = x
    else:
        parents[x] = y


while True:
    M,N = map(int,input().split())
    if (M,N) == (0,0):
        break
    lst = sorted(list(list(map(int,input().split()))for _ in range(N)),key=lambda x:x[2])
    sum_number = 0
    parents = [i for i in range(M)]
    for x,y,z in lst:
        if find_set(x) == find_set(y):
            sum_number += z
            continue
        union_set(x,y)

    print(sum_number)

# https://www.acmicpc.net/problem/6497
# 이 코드의 시간 복잡도는 O(N log N + M log M)
# sort하는데 O(N log N)
# 크루스칼 알고리즘은 O(log M)*O(M)
# 이유는 find_set이 최악의 경우 O(log M)
# 이것을 노드 수(M)만큼 돌리기 때문