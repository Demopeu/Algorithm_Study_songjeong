# 백준 12015번 가장 긴 증가하는 부분 수열 2

# 수열이 주어졌을 때 가장 긴 증가하는 부분 수열의 길이를 구하는 문제

# target이 들어갈 수 있는 적절한 위치를 찾는 함수
# 적절한 위치 -> target과 같은 값이 있다면 그 위치를 반환
# 만약 target과 같은 값이 없다면 그 값과 가장 가까우면서 그 값보다
# 작은 값과 큰 값 사이의 위치를 반환
def bin_search(start, end, target):
    if start > end:
        return start

    mid = (start + end) // 2
    temp = result[mid]

    if temp == target:
        return mid

    elif temp > target:
        return bin_search(start, mid - 1, target)

    else:
        return bin_search(mid + 1, end, target)

N = int(input())
num_list = list(map(int, input().split()))
result = [num_list[0]]

for i in range(1, N):
    # 현재 수가 result의 마지막 수보다 크다면 result에 추가
    if num_list[i] > result[-1]:
        result.append(num_list[i])

    # 마지막 수보다 작거나 같은 경우 이진 탐색을 통해
    # 그 수가 들어갈 수 있는 적절한 위치를 찾아서 
    # 그 자리의 값을 갱신
    else:
        result[bin_search(0, len(result) - 1, num_list[i])] = num_list[i]

print(len(result))


# 시간 복잡도 : O(N * log N)
# https://www.acmicpc.net/problem/12015