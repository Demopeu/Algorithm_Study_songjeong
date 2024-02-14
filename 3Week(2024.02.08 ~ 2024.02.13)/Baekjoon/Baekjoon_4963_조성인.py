# https://www.acmicpc.net/problem/4963

# 시간복잡도 : O(W * H)

# 섬의 땅을 지우는 함수 정의(함수 사용 이유 재귀로 여러번 호출하려고)
def remove_land(x, y):
    # 주변 8칸(12시부터 시계방향)
    move_x = [0,1,1,1,0,-1,-1,-1]
    move_y = [-1,-1,0,1,1,1,0,-1]

    # 현재 위치 땅을 지움
    matrix[x][y] = 0
    
    # 주변 8칸 탐색
    for n in range(8):
        moved_x = x + move_x[n]
        moved_y = y + move_y[n]
        
        # 맵 내에 있고 땅이 있다면
        if 0 <= moved_x < h and 0 <= moved_y < w and matrix[moved_x][moved_y] == 1:
            # 이 함수를 반복(인접한 땅이 모두 지워짐)
            remove_land(moved_x, moved_y)

while True:
    # 전체 맵의 너비 높이
    w, h = map(int, input().split())
    
    # 마지막 끝날 때 0,0이 주어지므로 종료
    if w == 0 and h == 0:
        break
    
    # 전체 맵 받기
    matrix = [list(map(int, input().split())) for _ in range(h)]
    
    # 섬의 갯수
    island = 0
    
    for i in range(h):
        for j in range(w):
            # 땅을 발견하면
            if matrix[i][j] == 1:
                # 인접한 땅을 지우기
                remove_land(i, j)
                # 섬 1개 추가
                island += 1
    
    # 섬이 다 사라지면 for문이 종료되고 섬의 개수를 출력
    print(island)