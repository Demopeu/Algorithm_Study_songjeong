# 백준 2110번 공유기 설치

# 공유기들을 적당히 설치해서 임의의 두 공유기 사이의 거리를
# 최대로 만들었을 때 그 거리를 구하는 문제
N, C = map(int, input().split())
num_list = [int(input()) for _ in range(N)]
num_list.sort()

start = 0
end = num_list[-1] - num_list[0]

while start <= end:
    # 이진 탐색 이용, left는 현재 공유기의 위치, cnt는 현재 공유기 개수
    mid = (start + end) // 2
    left = 0
    cnt = 1

    for i in range(N):
        # 만약 공유기로부터의 거리가 mid보다 크거나 같으면
        # 그 위치에 새로 공유기를 설치
        if num_list[i] - num_list[left] >= mid:
            cnt += 1
            left = i

    # 설치한 공유기의 개수가 C보다 작다면 end값을 작게 하고(거리가 너무 멀기 때문)
    # C보다 크거나 같으면 start값을 크게 하고(거리가 너무 가깝기 때문) mid를 result에 저장(최대)
    if cnt < C:
        end = mid - 1

    else:
        start = mid + 1
        result = mid

print(result)

# 시간 복잡도 : O(N * log E), E : 주어진 범위의 최대값과 최소값의 차이
# 문제 링크 : https://www.acmicpc.net/problem/2110