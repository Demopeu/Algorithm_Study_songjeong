# https://www.acmicpc.net/problem/17070

# pypy3
# DFS 사용
N = int(input())
MAP = [list(map(int,input().split())) for _ in range(N)]

# 파이프 타입,x,y
stack = [[0,1,0]]

cnt = 0
while stack:
    shape,x,y = stack.pop()
    # 마지막이 벽이면 바로 종료
    if MAP[N-1][N-1]:
        break
    # 마지막까지 도달하면 cnt+1
    if x == N-1 and y == N-1:
        cnt += 1
        continue
    # 파이프가 가로일 때
    if shape == 0:
        # 더 이상 이동 불가
        if x == N-1 and y < N-1:
            continue
        # 가로
        if x+1 < N and MAP[y][x+1] != 1:
            stack.append([0,x+1,y])
        # 대각선
        if x+1 < N and y+1 < N and MAP[y][x+1] != 1 and MAP[y+1][x] != 1 and MAP[y+1][x+1] != 1:
            stack.append([1,x+1,y+1])
    # 파이프가 대각선일 때
    if shape == 1:
        # 가로
        if x+1 < N and MAP[y][x+1] != 1:
            stack.append([0,x+1,y])
        # 대각선
        if x+1 < N and y+1 < N and MAP[y][x+1] != 1 and MAP[y+1][x] != 1 and MAP[y+1][x+1] != 1:
            stack.append([1,x+1,y+1])
        # 세로
        if y+1 < N and MAP[y+1][x] != 1:
            stack.append([2,x,y+1])
    # 파이프가 세로일 때
    if shape == 2:
        # 더 이상 이동 불가
        if x < N-1 and y == N-1:
            continue
        # 대각선
        if x+1 < N and y+1 < N and MAP[y][x+1] != 1 and MAP[y+1][x] != 1 and MAP[y+1][x+1] != 1:
            stack.append([1,x+1,y+1])
        # 세로
        if y+1 < N and MAP[y+1][x] != 1:
            stack.append([2,x,y+1])

print(cnt)