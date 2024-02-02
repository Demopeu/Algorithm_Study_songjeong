# 알고리즘 풀이

# 세로 가로 길이
N,M = map(int,input().split())

# 세로가 1일 때
# 나이트 이동불가
if N == 1:
    result = 1

# 세로가 2일 때
# 나이트는 오른쪽 2칸씩 이동
# 이동횟수가 4이상일 경우 이동방법에 제한
# 최대 4회 이동가능
elif N == 2:
    result = (M + 1) // 2
    if result >= 4:
        result = 4

# 세로가 3 이상일 때
else:
    # 가로의 길이가 7(기본 위치 + 모든 이동 종류의 가로 길이 합)미만일 때
    # 가로의 길이만큼 이동가능하나
    # 최대 4회 이동가능
    if M < 7:
        result = M
        if result >= 4:
            result = 4

    # 가로의 길이가 7이상(모든 종류의 이동을 수행가능)일 때
    # 5(모든 방법 1회 사용 시 이동횟수) + (M-7)(총 길이에서 먼저 사용한 이동거리만큼 차감)
    else:
        result = M - 2

print(result)

"""
엄
# 세로 가로 길이
N,M = map(int,input().split())

# 체스테이블
# chess_table = [[0] * M for _ in range(N)]
# 메모리 초과
# 대안 : 나이트 위치 기록 사용
knight_log = []

# 나이트 위치(세로, 가로)
knight = [N-1,0]

# index를 통한 이동에 따른 위치 변경값
# 무조건 오른쪽으로 전진해야 하므로 최대 이동횟수를 위해 오른쪽을 적게 이동하는 것부터 우선 배치
move_y = [-2,2,-1,1]
move_x = [1,1,2,2]

# 방문 횟수(시작 위치부터 카운트)
# 나이트 위치 기록의 길이로 대체
# visit = 1

# 나이트 시작 위치
# chess_table[knight[0]][knight[1]] = 1
knight_log.append(knight[:])

# 이동 기록
move_log = []

# 나이트가 체스판 오른쪽 끝에 갈 때까지 반복
while M - knight[1] > 1:

    # 이동 우선순위
    move_priority = [0,1,2,3]

    # 이동 기록이 4미만일 경우
    if len(move_log) < 4:
        for n in range(4):
            # 이동기록에 번호가 있으면
            if n in move_log:
                # 우선순위 후순위로 두기
                move_priority.remove(n)
                move_priority.append(n)

    # 우선순위대로 반복
    for move in move_priority:
        # 다음 이동이 체스판을 넘어가지 않으면
        if knight[1] + move_x[move] < M and 0 <= knight[0] + move_y[move] < N:
            # 이동을 실행
            knight[1] += move_x[move]
            knight[0] += move_y[move]
            # 이동기록에 해당 이동 번호 추가
            move_log.append(move)
            break
        # 다음 이동이 체스판을 넘어가면
        else:
            # 이동을 실행하지 않고 다음 우선순위로 넘어감
            continue

    # 이동을 하지 못했을 경우 종료
    # if chess_table[knight[0]][knight[1]] == 1:
    if knight in knight_log:
        break
    # 이동을 했을 경우 해당 위치에 1로 표시 후 방문 횟수 1추가
    else:
        # chess_table[knight[0]][knight[1]] = 1
        knight_log.append(knight[:])
        # visit += 1
    
    # 이동 4회 이상에 이동을 종류별로 하지 않았으면 종료
    # if visit > 4 and 0 not in move_log and 1 not in move_log and 2 not in move_log and 3 not in move_log:
    # all() : 파이썬 내장함수, 모든 요소가 참이면 True, 아니면 False 반환
    if len(knight_log) > 4 and all(i not in move_log for i in range(4)):
        break

# 결과값인 방문 횟수 출력
# print(visit)
# 나이트 위치 기록의 길이 = 방문횟수
print(len(knight_log))
"""