# https://www.acmicpc.net/problem/1920

N = int(input())
# set 사용
N_num = set(map(int,input().split()))
M = int(input())
M_num = list(map(int,input().split()))

for num in M_num:
    # in에 set을 사용
    # in list는 리스트의 원소를 하나씩 모두 비교하기 때문에 리스트가 클수록 느림
    # in set의 경우 set은 해시를 사용하기 때문에 리스트의 크기와는 상관없이 해시 함수 연산 시간만큼 걸림
    if num in N_num:
        print(1)
    else:
        print(0)