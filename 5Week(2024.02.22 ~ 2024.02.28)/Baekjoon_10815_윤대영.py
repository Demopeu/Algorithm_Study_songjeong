def binary_search(lst, num, start, end):
    if start > end:         # start가 end보다 크면 더 이상 탐색할 곳 없다는 뜻
        return 0

    mid = (start + end) // 2
    if lst[mid] == num:
        return 1
    elif lst[mid] > num:
        return binary_search(lst, num, start, mid - 1)
    else:
        return binary_search(lst, num, mid + 1, end)


n = int(input())    # 숫자 카드 n개
cards = sorted(list(map(int, input().split())))
m = int(input())    # 찾을 카드 m개
finds = list(map(int, input().split()))
finds_lst = []
# 존재 여부 finds_lst에 추가
for find in finds:
    finds_lst.append(binary_search(cards, find, 0, n - 1))

print(*finds_lst)




# 시간복잡도: O(m log n)
# 출처: https://www.acmicpc.net/problem/10815