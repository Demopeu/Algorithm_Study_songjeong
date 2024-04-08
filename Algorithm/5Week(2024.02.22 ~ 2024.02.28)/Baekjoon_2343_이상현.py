# 백준 2343번 기타 레슨

# M개의 블루레이로 모든 강의를 저장하려고 할 때 필요한
# 블루레이의 크기 중 최소를 구하는 문제
N, M = map(int, input().split())
lecture_list = list(map(int, input().split()))

# 최소한 가장 긴 강의만큼의 크기를 가져야하고,
# 최대의 경우 모든 강의를 한 번에 녹화 가능한 크기
start = max(lecture_list)
end = sum(lecture_list)

while start <= end:
    # temp는 현재 녹화 시작한 강의, cnt는 현재까지 사용된 블루레이 개수
    mid = (start + end) // 2
    temp = 0
    cnt = 1

    for i in range(N):
        temp += lecture_list[i]

        # 만약 블루레이 용량을 초과할 시 cnt를 1 증가하고
        # 녹화 시작 강의를 갱신
        if temp > mid:
            cnt += 1
            temp = lecture_list[i]

    # 만약 cnt가 M보다 작거나 같으면(블루레이 용량이 너무 큼) end를 작게 하고 mid를 저장(최소)
    # 만약 cnt가 M보다 크면(블루레이 용량이 너무 작음) start를 크게 함
    if cnt <= M:
        end = mid - 1
        result = mid

    else:
        start = mid + 1

print(result)

# 시간 복잡도 : O(N * logE), E : 강의 시간의 범위 : end - start
# 문제 링크 : https://www.acmicpc.net/problem/2343