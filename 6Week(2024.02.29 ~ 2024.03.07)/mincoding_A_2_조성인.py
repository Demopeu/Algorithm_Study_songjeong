T = int(input())

# 포를 움직이는 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for test_case in range(1, T + 1):
    # 맵 길이
    N = int(input())
    # 맵
    MAP = [list(map(int, input().split())) for _ in range(N)]
    # 죽인 말들 위치
    kill = []
    
    # 정지 플래그
    stop = False
    for i in range(N):
        for j in range(N):
            # 포를 발견하면 스택에 추가, 포 자리를 비움, 플래그 작동
            if MAP[i][j] == 2:
                stack = [[j, i, 0, []]]
                MAP[i][j] = 0
                stop = True
                break
        if stop:
            break

    # 스택이 있는 동안 반복
    while stack:
        # x좌표, y좌표, 이동 턴수, 현재 잡은 말
        [x, y, turn, killing] = stack.pop()
        
        # 이동을 3번 했으면 더 이상 다음 경우로 넘어감
        if turn == 3:
            continue
        
        # 4방향 순회
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            
            # 이동가능 상태
            move_able = False
            # 계속 반복
            while True:
                # 범위 밖을 벗어나면 종료
                if 0 > nx or nx >= N or 0 > ny or ny >= N:
                    break
                    
                # 이동가능일때
                if move_able:
                    # 빈곳이면
                    if MAP[ny][nx] == 0:
                        # 스택에 추가
                        stack.append([nx, ny, turn + 1, killing[:]])
                        # 다음 좌표 보기(while True에서 반복)
                        nx = nx + dx[l]
                        ny = ny + dy[l]
                    # 말이 있으면
                    else:
                        # 해당 말이 여태까지 잡히지 않았을때
                        if [nx, ny] not in kill:
                            # 현재 경로에서 잡은 말로 추가
                            killing.append([nx, ny])
                            # 전체 경로에서 잡은 말로 추가
                            kill.append([nx, ny])
                            # 이동 상태 변경 후
                            move_able = False
                            # 스택에 추가
                            stack.append([nx, ny, turn + 1, killing[:]])
                            break
                        # 해당 말이 잡혔지만
                        else:
                            # 현재 경로에서 잡은 말이 아니었을때
                            if [nx, ny] not in killing:
                                # 현재 경로에서 잡은 말로 추가
                                killing.append([nx, ny])
                                # 이동 상태 변경 후
                                move_able = False
                                # 스택에 추가
                                stack.append([nx, ny, turn + 1, killing[:]])
                                break
                            # 현재 경로에서 이미 잡힌 말이면
                            else:
                                # 없는 말이므로 다음 좌표로 넘어감
                                nx = nx + dx[l]
                                ny = ny + dy[l]
                
                # 이동불가일때
                else:
                    # 빈곳이면
                    if MAP[ny][nx] == 0:
                        # 다음 좌표를 봄
                        nx = nx + dx[l]
                        ny = ny + dy[l]
                    # 말이 있으면
                    else:
                        # 이동 가능한 상태로 바꾸고
                        move_able = True
                        # 다음 좌표를 봄
                        nx = nx + dx[l]
                        ny = ny + dy[l]

    print(f'#{test_case} {len(kill)}')