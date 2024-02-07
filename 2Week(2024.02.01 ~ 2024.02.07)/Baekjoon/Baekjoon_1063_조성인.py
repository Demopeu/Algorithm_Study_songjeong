# https://www.acmicpc.net/problem/1063

# 시간복잡도 : O(N^2)

# 킹과 돌의 위치, 이동횟수
king,stone,N = input().split()
# 이동횟수는 정수
N = int(N)

# 각 이동별 위치 변경값
move_dict = {'R': [0, 1],
             'L': [0, -1],
             'B': [1, 0],
             'T': [-1, 0],
             'RT': [-1, 1],
             'LT': [-1, -1],
             'RB': [1, 1],
             'LB': [1, -1]}

# 이동을 위치 변경값으로 변경
move_list = [move_dict.get(input()) for _ in range(N)]

# 체스판 그리기
chess_board = [[alpha+str(n) for alpha in ['A','B','C','D','E','F','G','H']] for n in range(8,0,-1)]

# 이동별로
for move in move_list:
    # 외부(i) 반복문 종료 break
    chess_break = False
    # 체스판 순회
    for i in range(8):
        for j in range(8):
            # 킹의 위치 찾기
            if chess_board[i][j] == king:
                # 킹이 이동 후 체스판 안에 있을 때
                if 0 <= i+move[0] < 8 and 0 <= j+move[1] < 8:
                    # 이동 후 돌과 만나면
                    if chess_board[i+move[0]][j+move[1]] == stone:
                        # 돌이 이동 후 체스판 안에 있을 때
                        if 0 <= i + move[0] * 2 < 8 and 0 <= j + move[1] * 2 < 8:
                            # 돌과 킹의 위치 변경 후 종료
                            stone = chess_board[i + move[0] * 2][j + move[1] * 2]
                            king = chess_board[i + move[0]][j + move[1]]
                            chess_break = True
                            break
                        # 돌이 체스판 밖으로 나가면
                        else:
                            # 이동 없이 종료
                            chess_break = True
                            break
                    # 돌과 만나지 않으면
                    else:
                        # 킹만 이동 후 종료
                        king = chess_board[i+move[0]][j+move[1]]
                        chess_break = True
                        break
                # 킹이 체스판 밖으로 나가면
                else:
                    # 이동 없이 종료
                    chess_break = True
                    break

        if chess_break:
            break

print(king)
print(stone)