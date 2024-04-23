from itertools import permutations

def kmp(per,per2):
    table = list(0 for _ in range(len(per)))
    i = 0
    for j in range(1,len(per)):
        while i > 0 and per[i] != per[j]:
            i = table[i-1]
        if per[i] == per[j]:
            i += 1
            table[j] = i

    count = 0
    i = 0

    for j in range(len(per2)-1):
        while i > 0 and per[i] != per2[j]:
            i = table[i-1]
        if per[i] == per2[j]:
            i += 1
            if i == len(per):
                count +=1
                i = table[i-1]

    return count == K

N = int(input())
lst = list(input() for _ in range(N))
K = int(input())
answer = 0

for i in list(permutations(lst,N)):
    per = "".join(i)
    answer += (kmp(per,per+per)+0)
print(answer)


# https://www.acmicpc.net/problem/1097
# 이 코드의 시간 복잡도는 O(N+M) 단,M은 Max(table) 일 줄 알았는데,
# gpt 님께서 O(N!*(N+M))이라하심
# permutations로 N!
# 누군가 보이어 무어 알고리즘으로 풀어줘