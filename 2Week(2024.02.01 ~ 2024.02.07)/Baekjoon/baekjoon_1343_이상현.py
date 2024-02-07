# 백준 1343번 폴리오미노

# 이 문제는 'X'와 '.'으로 이루어진 문자열을 'AAAA'와 'BB'로 'X'를 겹침없이
# 모두 덮어야 한다.

# 문자열을 입력받고 사전순으로 가장 앞서는 답을 출력해야 하기 때문에
# 우선 'XXXX'를 'AAAA'로 바꾸고 'XX'를 'BB'로 바꾼다. 그 결과를 
# -1과 함께 board 변수에 튜플로 저장
board = (input().replace('X' * 4, 'A' * 4).replace('X' * 2, 'B' * 2), -1)

# 만약 X가 빠짐없이 덮였으면 board[0]에는 'X'가 없어야 함. 따라서
# 'X'가 없으면 -> False -> 0. 즉, board[0]을 출력하고, 만약 'X'가
# 있으면 -> True -> 1. 즉, board[1]을 출력한다.
print(board['X' in board[0]])

# https://www.acmicpc.net/problem/1343