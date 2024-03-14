# https://www.acmicpc.net/problem/1003

#시간 초과
# T = int(input())

# 피보나치 함수에서 0이랑 1일 때 해당 카운트를 +1
# def fib(N):
#     global cnt_0,cnt_1
#     if N == 0:
#         cnt_0 += 1
#         return 0
#     elif N == 1:
#         cnt_1 += 1
#         return 1
#     else:
#         return fib(N-1) + fib(N-2)

# for test_case in range(1,T+1):
#     cnt_0 = 0
#     cnt_1 = 0
#     N = int(input())
#     fib(N)
#     print(cnt_0,cnt_1)

T = int(input())

# 피보나치 리스트
fib_list = [[1,0],[0,1]]
# N이 40까지로 제한이 걸려있어 40까지
for i in range(2,41):
    # 어떤 숫자 N의 0과 1이 나오는 수는 N-1과 N-2의 각각의 수의 합들과 같음, 리스트에 추가
    fib_list.append([fib_list[i-2][0]+fib_list[i-1][0],fib_list[i-2][1]+fib_list[i-1][1]])

# 숫자를 받아서 리스트의 0과 1이 나오는 횟수 출력
for tc in range(T):
    N = int(input())
    print(*fib_list[N])