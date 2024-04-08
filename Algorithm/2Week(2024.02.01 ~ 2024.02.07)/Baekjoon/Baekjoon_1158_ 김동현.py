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
'''
import sys

def josephus(N, K):
    result = []
    idx = 0

    for i in range(N):
        idx = (idx + K - 1) % (i + 1)
        result.insert(idx, i + 1)

    result_str = '<' + ', '.join(map(str, result)) + '>'
    print(result_str)

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    josephus(N, K)

요세푸스의 문제는 리스트에 요소를 삭제하지 않고 풀 수 있는 코드가 있음
이 때, 시간 복잡도는 O(N)
'''