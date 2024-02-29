# https://www.acmicpc.net/problem/1654

# 이게 왜 런타임 에러...(주석 없었음)
# 제로 디비전 에러(mid가 0인 경우)
# 0이 나오려면 최대 길이가 1밖에 안된다는건데 자를 필요가 없잖아
# K,N = map(int,input().split())
# length = [int(input()) for _ in range(K)]
#
# start = 0
# end = max(length)
#
# while start <= end:
#     mid = (start + end) // 2
#     count = 0
#
#     for i in range(K):
#         count += length[i] // mid
#
#     if count < N:
#         end = mid - 1
#
#     else:
#         start = mid + 1
#
# print(end)

# 랜선 갯수, 만들고 싶은 랜선 갯수
K,N = map(int,input().split())
# 랜선들의 길이
length = [int(input()) for _ in range(K)]

# 1부터 시작(위 코드처럼 0일때 최대 길이 end가 1이면 mid가 0이라 제로 디비전 에러)
start = 1
# 랜선 최대 길이(만들 수 있는 최대 길이)
end = max(length)

while start <= end:
    # 중앙값
    mid = (start + end) // 2
    # 중앙값을 기준으로 만들 수 있는 랜선 갯수
    count = 0
    
    # 각 랜선을 순회
    for i in range(K):
        # 만들 수 있는 갯수 카운트
        count += length[i] // mid
    
    # 만들고 싶은 랜선보다 부족하면
    if count < N:
        # 길이를 줄여보자
        end = mid - 1
    # 아니면
    else:
        # 길이를 늘려보자
        start = mid + 1

print(end)