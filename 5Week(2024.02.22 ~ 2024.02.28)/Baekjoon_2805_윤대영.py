n, m = map(int, input().split())    # n: 나무의 수, m: 나무의 길이
trees = list(map(int, input().split()))     # 나무의 높이 list
start = 1           # 나무의 높이 최솟값
end = max(trees)
max_high = 0        # 나무의 최대 높이
# 나무의 높이를 이진 탐색 이용해서 측정하는 반복문
while start <= end:
    max_len = 0     # 나무 길이
    mid = (start + end) // 2

    for tree in trees:
        if tree > mid:
            max_len += tree - mid

    if max_len > m:
        max_high = mid
        start = mid + 1
    elif max_len == m:
        max_high = mid
        break
    else:
        end = mid - 1

print(max_high)




# 시간복잡도: O(n log k)
# 출처: https://www.acmicpc.net/problem/2805