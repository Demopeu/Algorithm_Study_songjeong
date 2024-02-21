# https://www.acmicpc.net/problem/1303

# 시간복잡도 : O(N * M)

N,M = map(int,input().split())
battle = [list(input()) for _ in range(M)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 재귀함수 사용
def power(friendly,x,y):
    global count
    # 카운트 하고
    count += 1
    # 카운트 되었다고 남김
    battle[y][x] = 'C'
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and battle[ny][nx] == friendly:
            # 재귀 호출
            power(friendly,nx,ny)

W_total = 0
B_total = 0

for i in range(M):
    for j in range(N):
        count = 0
        # 흰옷일때
        if battle[i][j] == 'W':
            friendly = 'W'
            power(friendly,j,i)
            W_total += count**2
        # 검은옷일때
        elif battle[i][j] == 'B':
            friendly = 'B'
            power(friendly,j,i)
            B_total += count**2

print(W_total, B_total)