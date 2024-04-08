# https://www.acmicpc.net/problem/21736

# 이거 써도 되는건가요?(런타임 에러 관련 인터넷 검색에서 가져옴)
import sys
sys.setrecursionlimit(10**6)

# 시간복잡도 : O(N * M)

N,M = map(int,input().split())
campus = [list(input()) for _ in range(N)]

# 함수 설명
# 전체 맵(2차원) : 틀, O : 비어있는 공간(P도 비어있다고 간주), X : 차있는 공간
# I부터 시작해서 진행가능한 4칸 중 비어있는 공간을 채움(O => X)
# 이걸 재귀함수로 만들어서 계속 반복
# 그렇게 채우면서 사람이 있는 곳(P)에 가면 1을 카운트
# 최종적으로 진행가능한 칸이 모두 사라지면 종료
def meeting(x,y):
    global people
    move_x = [0,1,0,-1]
    move_y = [-1,0,1,0]
    # 사람을 만나면 만난 사람 +1
    if campus[y][x] == 'P':
        people += 1
    # 빈 곳 채우기
    campus[y][x] = 'X'
    # 4방향
    for n in range(4):
        new_x = x + move_x[n]
        new_y = y + move_y[n]
        if 0 <= new_x < M and 0 <= new_y < N and campus[new_y][new_x] != 'X':
            # 다음 빈칸에서 반복
            meeting(new_x,new_y)

# 만난 사람 수
people = 0

for i in range(N):
    for j in range(M):
        # 도연이 찾기
        if campus[i][j] == 'I':
            # 함수 작업 시작
            meeting(j,i)

# 못 만나면 TT
if people == 0:
    people = 'TT'

print(people)