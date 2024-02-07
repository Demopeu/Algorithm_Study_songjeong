# https://www.acmicpc.net/problem/2578

# 시간 복잡도 : O(1)

# 빙고판
matrix = [list(map(int,input().split())) for _ in range(5)]
# 사회자 번호 리스트
call_num = []
for _ in range(5):
    call_num.extend(list(map(int,input().split())))

# 빙고판의 숫자를 사회자 번호 리스트의 인덱스로 변경
for i in range(5):
    for j in range(5):
        matrix[i][j] = call_num.index(matrix[i][j])

# 빙고판의 빙고가 되는 순서리스트
bingo_list = []

# 빙고판의 각 줄에서 가장 마지막으로 불리는 번호가 빙고의 마지막 순서가 됨
# 빙고리스트에 각 줄의 마지막 인덱스 번호를 추가
for i in range(5):
    bingo_list.append(max(matrix[i]))
    bingo_list.append(max(matrix[j][i] for j in range(5)))
    
bingo_list.append(max(matrix[i][i] for i in range(5)))
bingo_list.append(max(matrix[4-i][i] for i in range(5)))

# 빙고리스트를 정렬
bingo_list.sort()

# 빙고가 3개가 되면 승리하므로 3-1번째
# 0번이 아닌 1번부터 부르기 때문에 +1
print(bingo_list[2]+1)