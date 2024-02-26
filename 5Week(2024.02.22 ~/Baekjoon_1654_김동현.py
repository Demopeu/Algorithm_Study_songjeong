# 이분 탐색의 기초
def binary_search(start,end):
    while start<= end:
        mid = (start+end)//2
        line = 0
        # 다 쪼개기
        for i in lst:
            line += i//mid

        if line >= N:
            start = mid + 1
        else:
            end = mid -1
    return end


K,N = map(int,input().split())
lst = list(int(input()) for _ in range(K))
start, end = 1,max(lst)
print(binary_search(start,end))

# 이 코드의 시간 복잡도는 O(NlogN)
    # 이진 탐색은 O(logN)인데 랜선다발에 비례함.
    # 랜선 다발을 N이라 했을 때, 전체 시간 복잡도는 O(NlogN)