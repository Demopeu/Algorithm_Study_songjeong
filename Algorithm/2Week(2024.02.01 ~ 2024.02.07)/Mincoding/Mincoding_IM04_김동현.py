import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    max_size = 0
    count = 0
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dic = {}
    for i in range(N):
        for j in range(N):
            if matrix[i][j] not in dic:
                dic[matrix[i][j]] = [[i,j]]
            else:
                dic[matrix[i][j]].append([i,j])
    for i in range(N):
        for j in range(N):
            if len(dic[matrix[i][j]]) == 1:
                del dic[matrix[i][j]]
    if dic == {}:
        print(f'#{test_case} 9')
    else:
        for i in dic.values():
            for j in range(len(i)-1):
                for k in range(j+1,len(i)):
                    if 0<=k<len(i):
                        x = i[k][0] - i[j][0]
                        y = i[k][1] - i[j][1]
                        if x >=0 and y >= 0:
                            answer = (x+1)*(y+1)
                            if answer > max_size:
                                count = 1
                                max_size = answer
                            elif answer == max_size:
                                count+=1

        print(f'#{test_case} {count}')

# https://pro.mincoding.co.kr/problem-step/22/level/141/detail/SAMSUNG_IM_04
            
