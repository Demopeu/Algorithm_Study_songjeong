paper_cnt = int(input())
matrix = [[0 for c in range(100)] for r in range(100)]
total_area = 0

for _ in range(paper_cnt):
    n, m = map(int, input().split())        # n : 왼쪽 변과의 거리, m : 아래쪽 변과의 거리
    start_r, start_c = n - 1, 99 - 10 - m
    # 가로, 세로 길이 10이므로 row, col 10만큼 반복
    for r in range(start_r, start_r + 10):
        for c in range(start_c, start_c + 10):
            matrix[r][c] = 1
# 색종이 총 넓이
for r in range(100):
    total_area += sum(matrix[r])

print(total_area)

# 시간 복잡도: O(paper_cnt + 100 * 100)
# 출처: https://www.acmicpc.net/problem/2563
