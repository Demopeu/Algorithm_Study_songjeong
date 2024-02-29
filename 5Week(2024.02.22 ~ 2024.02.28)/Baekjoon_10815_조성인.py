# https://www.acmicpc.net/problem/10815

N = int(input())
# set 사용
N_cards = set(map(int,input().split()))
M = int(input())
M_cards = list(map(int,input().split()))

# 리스트 순회
for i in range(M):
    # in 사용 시 리스트는 모든 원소를 일일이 비교하므로 리스트가 커질수록 느림
    # set은 해시를 사용, 해시함수 연산 시간만큼 걸림
    # in list => O(n)
    # in set => O(1)
    if M_cards[i] in N_cards:
        print(1,end=' ')
    else:
        print(0,end=' ')