import sys
input = sys.stdin.readline

# 이동 방향을 정의한 리스트
direction = [[1,0], [0,1], [1,1], [-1,0], [0,-1], [-1,-1], [1,-1], [-1,1]]

def traverse(matrix, i, j):  # 인접한 섬 탐색하는 재귀함수
    if matrix[i][j] == 0:  # 현재 좌표 바다면 종료
        return

    matrix[i][j] = 0  # 방문한 좌표 0으로 변경
    for d in direction:  # 인접한 8방향
        ny = i + d[0]
        nx = j + d[1]
        if nx < 0 or ny < 0 or nx >= x or ny >= y:  # 다음 좌표가 범위를 벗어나면 넘어감
            continue
        if matrix[ny][nx] == 1:  # 다음 좌표가 육지인 경우
            traverse(matrix, ny, nx)  # 해당 좌표에서 다시 탐색 수행

def countIsland(x, y, matrix):  # 섬의 개수를 세는 함수
    count = 0  # 개수 초기화
    for i in range(y):
        for j in range(x):
            if matrix[i][j] == 1:  # 현재 좌표가 육지인 경우
                count += 1  # 개수 1 증가
                traverse(matrix, i, j)  # traverse 함수로 해당 좌표 주변 탐색

    return count  # 섬 개수 반환

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:  # 입력이 0 0인 경우 종료
        break
    matrix = [list(map(int, input().split())) for _ in range(y)]

    print(countIsland(x, y, matrix))

'''
시간 복잡도 O(nm), gpt 첨언
주어진 코드의 시간 복잡도는 O(n * m) 입니다. 여기서 n은 열의 개수를 의미하고, m은 행의 개수를 의미합니다.
countIsland 함수에서 이중 반복문을 사용하여 모든 좌표를 확인합니다.
이 때, 열의 개수를 n으로, 행의 개수를 m으로 나타내므로 시간 복잡도는 O(n * m)입니다.
traverse 함수는 재귀적으로 호출되지만, 각 좌표는 최대 한 번씩만 방문하므로 좌표의 개수에 비례하는 시간이 소요되지 않습니다.
따라서 전체 코드의 시간 복잡도는 O(n * m)입니다.
https://www.acmicpc.net/problem/4963
'''