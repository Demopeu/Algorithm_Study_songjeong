# 백준 2473번 세 용액

# 세 수의 합이 최대한 0에 가까운 세 수를 구하는 문제
N = int(input())
list_ = sorted(map(int, input().split()))
min_ = float('inf')

# 기본적으로 list_[i]의 수를 선택
for i in range(N):
    # list_[i]를 제외하고 2개를 선택
    rest = list_[:i] + list_[i + 1:]
    left = 0
    right = N - 2

    while left < right:
        # temp는 현재 두 수의 합
        temp = rest[left] + rest[right]

        # 만약 세 수의 합이 기존에 저장된 값보다 더 0에 가깝다면
        # min_값을 갱신하고 세 수를 result에 저장
        if abs(temp + list_[i]) < min_:
            min_ = abs(temp + list_[i])
            result = [rest[left], rest[right], list_[i]]

        else:
            # 만약 음수 쪽으로 멀리 있는 경우 left를 1 증가
            # 양수 쪽으로 멀리 있는 경우 right를 1 증가
            if temp + list_[i] < min_:
                left += 1
            else:
                right -= 1

# 오름차순으로 출력
print(*sorted(result))

# 시간 복잡도 : O(N ** 2)
# 문제 링크 : https://www.acmicpc.net/problem/2473