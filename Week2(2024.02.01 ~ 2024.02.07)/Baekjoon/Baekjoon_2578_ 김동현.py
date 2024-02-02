import sys
input = sys.stdin.readline

def find_bingo(matrix,number):
    num = 0
    if number<12:                                           # 5*5 매트릭스에서 12개 이상 X가 되야 빙고 3줄 가능
        return num
    # 가로
    for i in range(5):
        if all(matrix[i][j] == 0 for j in range(5)):        # all 구문 이용해서 전부 0인 경우 빙고 +1
            num += 1                                        # 원래 그냥 matrix[i]하고 all 써도 되는데 백준에서 틀렸습니다 나길래 걍 바꿈 무슨 이유일까?
    for i in range(5):
        if all(matrix[j][i] == 0 for j in range(5)):
            num += 1
    # 대각선
    if all(matrix[i][i] == 0 for i in range(5)):
        num += 1
    if all(matrix[i][4 - i] == 0 for i in range(5)):
        num += 1
    return num

matrix = [list(map(int, input().split())) for _ in range(5)]
number = 0

for _ in range(5):                                         # for문 이렇게 많이 쓰고 싶지 않은데 어짜피 O(1)짜리라서 막씀 
    lst = list(map(int,input().split()))                   # break 사용하려면 차라리 break 구문이 좋은듯 최대 25개라 속도도 별 차이 없음
    for k in range(5):
        for i in range(5):
            terminal = False                               # 줄보는 구문도 탈출 해야해서 34, 37 참조
            for j in range(5):
                if lst[k] == matrix[i][j]:
                    matrix[i][j] = 0
                    number += 1
                    terminal = True
                    break

            if terminal:
                break
        binggo_num = find_bingo(matrix,number)              # 처음에는 for 문 안에 def 안쓰고 구현 했다가 너무 구려보여서 위로 올림
        if binggo_num >= 3:
            print(number)
            sys.exit()                                      # 3개 이상 찾으면 그냥 시스템 자체를 종료


# https://www.acmicpc.net/problem/2578
            
# 이 코드의 시간 복잡도는 O(1)
            # 매트릭스가 고정되어 잇어서 O(1)
            # 반복이 각 반복문 내에 최대 5번 반복하므로 O(125)
            # def 사용시 반복문이 있으므로 O(1)
            # 따라서 O(1)