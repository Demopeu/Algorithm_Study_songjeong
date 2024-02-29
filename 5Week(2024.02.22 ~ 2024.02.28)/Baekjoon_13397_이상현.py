# 백준 13397번 구간 나누기 2

# 기타 레슨과 비슷한 문제
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

start = 0
end = max(num_list) - min(num_list)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    max_ = min_ = num_list[0]

    for i in range(N):
        max_ = max(max_, num_list[i])
        min_ = min(min_, num_list[i])

        if max_ - min_ > mid:
            cnt += 1
            max_ = min_ = num_list[i]

    if cnt <= M:
        end = mid - 1
        result = mid

    else:
        start = mid + 1

print(result)

# 시간 복잡도 : O(N * log E), E : 주어진 범위의 최대값과 최소값 차이
# 문제 링크 : https://www.acmicpc.net/problem/13397