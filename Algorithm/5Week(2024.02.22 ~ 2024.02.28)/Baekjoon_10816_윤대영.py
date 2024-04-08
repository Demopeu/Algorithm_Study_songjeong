import sys
input = sys.stdin.readline

def binary_search(lst, target, start, end):     # 시간 초과 후 반복문으로 변경
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return 1, mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0, -1


n = int(input())    # 숫자 카드 n개
cards = list(map(int, input().split()))
m = int(input())    # 찾을 카드 m개
finds = list(map(int, input().split()))
find_lst = []

cards.sort()        # 시간 초과로 sorted -> sort로 변경

for find in finds:
    result, idx = binary_search(cards, find, 0, n - 1)
    if result == 1:
        start_idx, end_idx = idx, idx   # 시작 idx, 끝 idx
        while start_idx > 0 and cards[start_idx] == cards[start_idx - 1]:
            start_idx -= 1
        while end_idx < n - 1 and cards[end_idx] == cards[end_idx + 1]:
            end_idx += 1
        find_lst.append(end_idx - start_idx + 1)
    else:
        find_lst.append(0)

print(*find_lst)




# 시간복잡도: O(n log n)
# 출처: https://www.acmicpc.net/problem/10816