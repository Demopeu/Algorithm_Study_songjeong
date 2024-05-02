N = int(input())
dic = {}
for i in range(N):
    fileName = input()
    for j in range(len(fileName)):
        dic[j] = fileName[j] if j not in dic else '?' if dic[j] != fileName[j] else dic[j]
print(''.join(list(dic.values())))

# https://www.acmicpc.net/problem/1032
# 파이썬 재활의 일환

