import sys
input = sys.stdin.readline

def binary_search(start,end):

    while start<= end:
        mid = (start+end)//2
        sum_tree = 0

        for i in range(len(lst)):
            if lst[i] > mid:
                sum_tree += lst[i] - mid


        if sum_tree >= M:
            start = mid + 1
        else:
            answer = mid-1
            end = mid-1

    return answer


N,M = map(int, input().split())
lst = list(map(int, input().split()))
start,end = 1,max(lst)
print(binary_search(start,end))

#https://www.acmicpc.net/problem/2805
# 주석 추후기입