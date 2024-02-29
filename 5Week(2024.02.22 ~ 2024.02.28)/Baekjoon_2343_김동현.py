import sys
input = sys.stdin.readline

def BinarySearch(start, end):

    while start <= end:
        mid = (start + end) // 2
        sum_number = 0
        count = 1

    # 개수보다 크면 자르고 새로 더하기
        for i in range(N):
            if sum_number + lst[i] > mid:
                count += 1
                sum_number = 0
            sum_number += lst[i]

        if count > M:
            start = mid + 1

        else:
            answer = mid
            end = mid - 1

    return answer

N,M = map(int, input().split())
lst = list(map(int, input().split()))
start,end = max(lst),sum(lst)
print(BinarySearch(start,end))

# https://www.acmicpc.net/problem/2343
# 시간 초과 난 코드
# 이거 걍 if,else에 >=,>랑 answer = mid 바꾸면서 해서 맞춤
# 감을 못잡겟다
'''
def BinarySearch(start, end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        count = 0
        now = 0

        for i in range(len(lst)):
            if now == len(lst) - 1:
                count += 1
                break
            if sum(lst[now:i + 1]) > mid:
                count += 1
                now = i
        if count >= M:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1

    return answer
'''
