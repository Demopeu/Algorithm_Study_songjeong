T = int(input())

for test_case in range(1,T+1):
    # 나무 수
    N = int(input())
    # 나무들의 높이
    trees = list(map(int,input().split()))
    # 목표로 할 나무 높이
    goal = max(trees)

    # 나무 높이를 부족한 높이로 변경
    for i in range(N):
        trees[i] = goal - trees[i]

    # 부족한 높이 순으로 정렬
    trees.sort()

    # 일수
    day = 0
    # 모든 나무가 부족한 높이가 0이 되면 종료
    while set(trees) != {0}:
        # 일수 추가
        day += 1
        for i in range(N):

            # 이미 목표 높이인 나무 건너뛰기
            if trees[i] == 0:
                continue

            # 홀수 일째(1 주기)
            if day % 2 == 1:
                # 남은 높이가 2고 2가 남은 나무가 하나면 건너뛰기
                # 1을 주면 안되는 경우(1을 주면 이틀을 기다려야 하지만 안 주면 하루만 기다리면 됨)
                if trees[i] == 2 and trees.count(2) == 1:
                    continue
                trees[i] -= 1
                break

            # 짝수 일째(2 주기)
            else:
                # 2보다 작으면 목표 높이보다 높아지므로 건너뜀
                if trees[i] < 2:
                    continue
                trees[i] -= 2
                break

    print(f'#{test_case} {day}')

# 상현 코드
# T = int(input())

# for test_case in range(1,T+1):
#     # 나무 수
#     N = int(input())
#     # 나무들의 높이
#     trees = list(map(int,input().split()))
#     # 목표로 할 나무 높이
#     goal = max(trees)

#     # 1을 주는 경우
#     count1 = 0
#     # 2를 주는 경우
#     count2 = 0

#     # 나무 높이를 부족한 높이로 변경
#     for i in range(N):
#         trees[i] = goal - trees[i]
#         # 2로 나눈 나머지(반드시 1이 필요)
#         count1 += trees[i] % 2
#         # 2로 나눈 몫(2를 사용하는 경우)
#         count2 += trees[i] // 2
    
#     # 1을 주는 경우가 2를 주는 경우 이상이 될때 종료
#     while count1 + 1 < count2:
#         # 2를 주는 경우를 1을 주는 경우 2번으로 바꿈
#         count1 += 2
#         count2 -= 1
    
#     # 각 경우의 수에 따라 결과 변경
#     if count1 > count2:
#         result = 2 * count2 + 1
#     else:
#         result = 2 * count2

#     print(f'{test_case} {result}')