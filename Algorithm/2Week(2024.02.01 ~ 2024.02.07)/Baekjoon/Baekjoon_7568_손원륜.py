T = int(input())

lst = [list(map(int, input().split())) for _ in range(T)]   # lst에 데이터 저장

for i in lst:
    rank = 1            # rank 초기값
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:     # 다른 데이터와 비교하여 몸무게, 키 둘 다 작으면 랭크+1
                rank += 1
    print(rank, end=' ')      # 줄넘김없이  ' '공백 후 프린트 이어가기