import sys
input = sys.stdin.readline

def dfs(x, y):
    stack = []                                                              # stack = [[x,y]] 해도 되는데 그냥 시름
    stack.append([x,y])

    while stack:

        node = stack.pop()

        if not visited[node[0]][node[1]]:                                   # x,y의 방문을 확인하고 실행

            visited[node[0]][node[1]] = True                                # 방문으로 변경

            for l in range(4):                                              # 2차원 배열 상하좌우 확인하는 로직

                new_i = node[0]+dx[l]
                new_j = node[1]+dy[l]

                if 0<= new_i < N and 0<= new_j < M and fild[new_i][new_j]:  # 만일 2차원 배열 안에 들어가고 배추가 심어져 있을 경우
                    stack.append([new_i,new_j])                             # 스택에 추가


# 혹시 while 쓰기 싫다하는 사람을 위한 재귀문(하지만 이 문제에서는 최대 재귀 깊이 초과 뜸)
                    
'''
def dfs(x,y):
    visited[x][y] = True

    for l in range(4):
        new_i = x + dx[l]
        new_j = y + dy[l]

        if 0 <= new_i < N and 0 <= new_j < M and fild[new_i][new_j]:
            dfs(new_i,new_j)
'''


T = int(input())

for test_case in range(1, T + 1):

    # 변수 설정
    M, N, K = map(int, input().split())
    bechu = [list(map(int, input().split())) for _ in range(K)]
    count = 0                                                               # 지렁이의 수

    # 좌표계 설정
    dx = [0, 1, 0, -1]                                                      
    dy = [1, 0, -1, 0]


    # 2차원 배열 설정 밑 밑작업
    visited = [[False for _ in range(M)] for _ in range(N)]                 # 방문을 2차원 배열로
    fild = [[0 for _ in range(M)] for _ in range(N)]                        # 밭을 2차월 배열로
    
    for i in bechu:                                                         # 밭에 배추를 1로 표현
        fild[i[1]][i[0]] = 1                                                

    # 방문하지 않은 배추의 위치에서 dfs를 실행
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and fild[i][j] == 1:
                count += 1
                dfs(i,j)

    # 지렁이의 값 출력
    print(count)


# 이 코드의 시간 복잡도는 O(N*M)
    # dfs 함수 내의 while 반복은 좌표의 개수에 비례한 시간이 소요되는데
    # 일반적으로 O(1)의 시간 복잡도를 가진다고 함
    # 따라서 이중 반복문의 시간 복잡도인 O(N*M)를 따라감