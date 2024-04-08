N = input()
dic = {i:0 for i in range(10)}
for i in N:
    i = int(i)
    dic[i] += 1
uturn = dic[6]+dic[9]
if uturn % 2 == 0:
    dic[6] = uturn// 2
else:
    dic[6] = uturn // 2 + 1
dic[9] = uturn // 2
print(max(dic.values()))

# https://www.acmicpc.net/problem/1475
            
# 이 코드의 시간 복잡도는 O(N)
            # 반복문 N 단 하나!
            # 따라서 O(N*log(N))