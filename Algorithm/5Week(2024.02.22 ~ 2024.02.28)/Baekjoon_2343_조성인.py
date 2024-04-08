# https://www.acmicpc.net/problem/2343

# 강의 수, 블루레이 수
N,M = map(int,input().split())
# 강의 길이 리스트
length = list(map(int,input().split()))

# 시작점 : 강의 최대 길이
start = max(length)
# 끝점 : 강의 총 길이
end = sum(length)

while start <= end:
    # 중앙 값 : 자를 구간의 최대 길이
    mid = (start + end) // 2
    # 구간별 길이 합
    sum_ = 0
    # 구간 개수
    count = 1
    for i in range(N):
        # 구간 길이에 추가
        sum_ += length[i]
        # 구간 길이가 최대 길이보다 커지면
        if sum_ > mid:
            # 다음 구간에 넣음
            sum_ = length[i]
            # 구간 +1
            count += 1
    # 구간(블루레이)이 블루레이 수보다 작거나 같을 때
    if count <= M:
        result = mid
        end = mid - 1
    # 아닌 경우
    else:
        start = mid + 1

print(result)