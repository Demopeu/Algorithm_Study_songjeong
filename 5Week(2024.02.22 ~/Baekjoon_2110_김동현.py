def binary_search(start,end):
    answer = 0
    while start<= end:
        mid = (start+end)//2
        count = 1
        now = lst[0]

        # 거리를 체크 하는 수식
        for i in range(1,len(lst)):
            if lst[i] >= now + mid:
                count += 1
                now = lst[i]

        if count >= C:
            answer = mid
            start = mid + 1
        else:
            end = mid-1
    return answer


N,C = map(int,input().split())
lst = list(int(input()) for _ in range(N))
lst.sort()
start, end = 1,lst[-1]-lst[0]               # lst[-1]-lst[0] 거리
print(binary_search(start,end))

# 이분 탐색 말고 풀이법이 있을 까해서 처음에는 [0]*lst[-1] 배열로 했는데 틀림
# 두번째는 시간 초과가 나길래 도저히 못풀겟어서 인터넷 찾아봄
# 근데 알고보니 이분 탐색해도 아슬아슬하게 되서 주석을 모두 지우고 하니까 통과됨

# 이 코드의 시간 복잡도는 O(N log N)
    # 이진 탐색이 log(N)번 반복, lst 배열 순회하며 거리 체크 하니까 O(N) 곱해주니까
    # O(N log N)
