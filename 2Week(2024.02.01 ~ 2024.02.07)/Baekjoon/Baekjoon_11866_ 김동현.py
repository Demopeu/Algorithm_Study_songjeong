import sys
input = sys.stdin.readline

N,K = map(int,input().split())
idx= 0
lst = list(i for i in range(1,N+1))
yosepusu = []
while len(lst)>1:
    idx = (idx+K-1)%len(lst)                        #  원형이기 때문에 인덱스 조정
    yosepusu.append(lst.pop(idx))
yosepusu.append(lst[0])
result_str = '<' + ', '.join(map(str, yosepusu)) + '>'
print(result_str)

# https://www.acmicpc.net/problem/1158
            
# 이 코드의 시간 복잡도는 O(N*K)
            # K가 무한히 증가할 경우, O(N^2)

# 요세푸스 문제랑 머가 다른거지?