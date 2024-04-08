# 이분 탐색의 기초
def binary_search(start,end,target):

    while start <= end:
        mid = (start+end)//2

        if A[mid] == target:

            return 1

        elif A[mid]> target:

            end = mid -1

        else:
            start = mid + 1

    return 0


N = int(input())
A = list(map(int,input().split()))
A.sort()                                # 무조건 정렬해야함
M = int(input())
lst = list(map(int,input().split()))

for i in lst:
    start,end = 0, N-1
    print(binary_search(start,end,i))

## https://www.acmicpc.net/problem/1920
# 이 코드의 시간 복잡도는 O(NlogN)
    # 이진 탐색은 O(logN)인데 sort 써서 O(NlogN)