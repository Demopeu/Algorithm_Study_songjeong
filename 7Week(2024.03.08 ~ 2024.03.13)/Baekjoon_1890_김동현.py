import sys
input = sys.stdin.readline

N = int(input())
matrix = list(list(map(int,input().split()))for _ in range(N))
check = [[0]*N for _ in range(N)]
check[0][0] = 1

dx = [0,1]
dy = [1,0]

# 완전 탐색이 아닌 지나가는 길만 체크를 함
# dfs는 아닌 길도 전부 끝까지 가보는 거에 반면 이 프로그램은 check = 0 or matrix = 0
# 이면 거르도록 설정
for i in range(N):
    for j in range(N):
        '''
        num = matrix[i][j]
        if num == 0:
            print(check[i][j])
            
        이렇게 했다가 51퍼에서 오류남
        히든 testcase에 matrix[i][j] == 0 이 있음
        '''
        if i == N-1 and j == N-1:
            print(check[i][j])
            break
        
        num = matrix[i][j]
        # num = 0 이면 걍 거르도록
        if num and check[i][j]:
            for l in range(2):
                nx = i + dx[l]*num
                ny = j + dy[l]*num
                if 0<= nx < N and 0<=ny < N:
                    check[nx][ny] += check[i][j]

# https://www.acmicpc.net/problem/1890
# 시간 복잡도는 O(N^2)

# 아래는 시간 초과 난 코드 1초라고 해서 될 줄 알앗는데 안됨
'''
def dfs(start):
    queue = [start]
    count = 0
    while queue:
        x,y = queue.pop()
        if matrix[x][y] == 0:
            count += 1
            continue
        for l in range(2):
            nx = x+dx[l]*matrix[x][y]
            ny = y+dy[l]*matrix[x][y]

            if 0<= nx < N and 0<=ny < N:
                queue.append((nx,ny))
    return count


N = int(input())
dx = [0,1]
dy = [1,0]
matrix = list(list(map(int,input().split()))for _ in range(N))
print(dfs((0,0)))

'''
