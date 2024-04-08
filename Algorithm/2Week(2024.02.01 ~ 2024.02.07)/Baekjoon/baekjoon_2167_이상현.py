# 백준 2167번 2차원 배열의 합

# 이 문제의 난이도는 어렵지 않은 편
# 입력으로 주어지는 행렬을 list_에 저장
N, M = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(N)]

# 합을 구할 부분을 index_list에 저장
K = int(input())
index_list = [list(map(int, input().split())) for _ in range(K)]

# index_list에 저장된 각 합을 구할 부분마다
# 행렬의 값의 합을 구하여 출력함
for index in index_list:
    sum_ = 0

    for row in range(index[0] - 1, index[2]):
        for col in range(index[1] - 1, index[3]):
            sum_ += list_[row][col]

    print(sum_)

# https://www.acmicpc.net/problem/2167