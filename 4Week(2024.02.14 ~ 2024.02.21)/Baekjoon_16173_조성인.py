# https://www.acmicpc.net/problem/16173

# 시간복잡도 : O(N^2)

N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]

# 스택 사용(각 이동시 젤리의 위치 저장)
stack = [[0,0]]

# 결과 기본값
result = 'Hing'
# 스택이 존재하는 동안
while stack:
    [y,x] = stack.pop()
    # 도달하는 경우가 있으면 결과를 변경
    if matrix[y][x] == -1:
        result = 'HaruHaru'
    else:
        n = matrix[y][x]
        # 0인 경우 무한루프이므로 다음 좌표로 넘어감
        if n == 0:
            continue
        # 범위 밖으로 벗어나지 않는 경우 스택에 넣음
        if y + n < N:
            stack.append([y + n, x])
        if x + n < N:
            stack.append([y, x + n])

print(result)