def binary_search(lst, num, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if lst[mid] == num:
        return 1
    elif lst[mid] > num:
        return binary_search(lst, num, start, mid - 1)
    else:
        return binary_search(lst, num, mid + 1, end)


t = int(input())

for tc in range(1, t + 1):
    n = int(input())    # 수첩 1의 정수 개수
    note1 = sorted(list(map(int, input().split())))     # 이진 탐색은 list '정렬' 필수
    m = int(input())    # 수첩 2의 정수 개수
    note2 = list(map(int, input().split()))

    for note in note2:
        print(binary_search(note1, note, 0, n - 1))




# 시간복잡도: O(m log n)
# 출처: https://www.acmicpc.net/problem/2776