N = int(input())
mamoization = [0]*21
mamoization[0] = 1
mamoization[1] = 1
for i in range(2,21):
    if i%2 != 0:
        mamoization[i] = mamoization[i-1]*2
    else:
        mamoization[i] = mamoization[i-1]*2 - (mamoization[i-4] + mamoization[i-5])
print(mamoization[N])

# N = int(input())
# mamoization = {i:0 for i in range(21)}
# death = {i:0 for i in range(25)}
# mamoization[1] = 1
# death[4] = 1
# for i in range(2,N+1):
#     if i%2 == 0:
#         death[i+4] += mamoization[i-1]
#     else:
#         death[i+3] += mamoization[i-1]
#     mamoization[i] = mamoization[i-1]*2 - death[i]
# print(mamoization[N])

# https://www.acmicpc.net/problem/17291
# DP 생각이 안났어