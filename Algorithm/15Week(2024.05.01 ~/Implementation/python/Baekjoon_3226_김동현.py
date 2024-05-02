import sys
input = sys.stdin.readline

N,answer= int(input()),0
for _ in range(N):
    time,DD = input().split(' ');DD=int(DD);
    HH,MM=map(int,time.split(':'))
    end_HH = (HH + (MM + DD) // 60)%24
    if not((HH == 6 and end_HH == 7) or (HH==18 and end_HH == 19)):
        answer += DD*10 if 6<HH<19 else DD*5
    else:
        answer += (MM+DD-60)*10+(DD-(MM+DD-60))*5 if 6<end_HH<19 else (MM+DD-60)*5+(DD-(MM+DD-60))*10
print(answer)

# https://www.acmicpc.net/problem/3226
# 파이썬 재활의 일환
