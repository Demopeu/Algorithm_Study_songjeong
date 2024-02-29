# https://www.acmicpc.net/problem/1072

# 시간복잡도 : O(log(N)), N은 mid의 가능한 값의 범위

# 계산(런타임 에러)
# O(1)
# import math
#
# X,Y = map(int,input().split())
# Z = int(Y*100/X)
#
# if Y * 100 / X >= 99:
#     print(-1)
# else:
#     lose = X-Y
#
#     result = math.ceil(100/(100-Z-1) * lose) - X
#
#     print(result)

# 판수, 이긴판
X,Y = map(int,input().split())
# 현재 승률
Z = Y*100/X
# 시작과 끝
start,end = 1,1000000000

# 이분 탐색
while start <= end:
    # 중앙값
    mid = (start + end) // 2
    # 중앙값을 더한 승률이 원래 승률보다 크면
    if int(((Y + mid) * 100 / (X + mid))) > Z:
        # 끝 지점을 옮김
        end = mid - 1
    # 중앙값을 더한 승률이 원래 승률과 같거나 작으면
    else:
        # 시작 지점을 옮김
        start = mid + 1

# 승률이 오르지 않는 경우(99% 이상인 경우)
if Y * 100 / X >= 99:
    print(-1)
else:
    print(start)