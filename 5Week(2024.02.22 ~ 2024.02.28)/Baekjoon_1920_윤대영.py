def binary_search(lst, target, start, end):
    if start > end:     # end가 start보다 크다면 더 이상 탐색할 곳 없다는 뜻(target 없다는 뜻)
        return 0

    mid = (start + end) // 2
    if lst[mid] == target:
        return 1
    elif lst[mid] > target:
        return binary_search(lst, target, start, mid - 1)    # 왼쪽 범위 탐색
    else:
        return binary_search(lst, target, mid + 1, end)      # 오른쪽 범위 탐색


n = int(input())    # n: 정수의 개수
num_lst = sorted(list(map(int, input().split())))
m = int(input())    # m: num_lst에서 찾아야할 수의 개수
find_lst = list(map(int, input().split()))

for find in find_lst:
    print(binary_search(num_lst, find, 0, n - 1))




# 시간복잡도: O(log n)
# 출처: https://www.acmicpc.net/problem/1920