n, m = map(int, input().split())    # 행렬 a의 크기 n * m
a = [list(map(int, input().split())) for r in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for r in range(m)]
b = list(map(list, zip(*b)))        # b 행렬 회전
muti_matrix = []

for row1 in a:
    for row2 in b:
        muti_matrix.append(list(map(lambda r1, r2 : r1 * r2, row1, row2))) # 행렬 곱들 muti_matrix에 append

muti_matrix = list(map(sum, muti_matrix))

for idx, num in enumerate(muti_matrix):     # 2차원 배열처럼 보이게 출력
    if (idx + 1) % n != 0:
        print(num, end=' ')
    else:
        print(num)

# 시간 복잡도: O(nmk)
# 출처: https://www.acmicpc.net/problem/2740
