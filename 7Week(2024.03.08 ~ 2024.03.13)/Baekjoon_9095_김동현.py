import sys
input = sys.stdin.readline
T = int(input())
# N은 최대 11개라길래 미리 동적으로 짬
memory = [0]*(12)
memory[1] = 1
memory[2] = 2
memory[3] = 4

for test_case in range(1,T+1):
    N = int(input())
    # 미리 계산되어 있으면 패스
    if memory[N] != 0:
        pass
    else:
        # 걍 3개 해보고 대충 해봣는데 맞았음
        for i in range(4,N+1):
            memory[i] = memory[i-1] + memory[i-2] + memory[i-3]
    print(memory[N])

# https://www.acmicpc.net/problem/9095
# 시간 복잡도는 O(N^2)

