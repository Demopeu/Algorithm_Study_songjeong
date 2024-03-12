import sys
input = sys.stdin.readline
N = int(input())
memory = [0]*(N+1)
memory[1] = 1
# 99퍼에서 틀려서 보니까 1일때 memory[2] = 2 넣어서 인덱스 에러남
if N == 1:
    print(1)
else:
    memory[2] = 2
    
    # 걍 이런거 할때 마다 3개까지 해보고 더하고 빼고 2* 양변까지 무지성으로 해보고
    # 안되면 고민 하기 시작
    for i in range(3,N+1):
        memory[i] = memory[i-1] + memory[i-2]
    print(memory[N]%10007)


# https://www.acmicpc.net/problem/11726
# 시간 복잡도는 O(N)

