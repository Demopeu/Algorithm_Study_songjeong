N = int(input())
lst = ''.join(list(input() for _ in range(N)))
dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
start = 0; end = N-1;
answer = ''
while start< end:
    if dic.index(lst[start])<dic.index(lst[end]):
        answer += lst[start];start += 1;
    elif dic.index(lst[start])>dic.index(lst[end]):
        answer += lst[end];end -= 1;
    else:
        flag = False
        new_start = start+1
        new_end = end-1
        while new_start<new_end:
            if dic.index(lst[new_start]) > dic.index(lst[new_end]):
                flag = True;break;
            elif dic.index(lst[new_start]) < dic.index(lst[new_end]):
                flag = False;break;
            else:
                new_start += 1;new_end -= 1;
        if flag:
            answer += lst[end];end -= 1;
        else:
            answer += lst[start];start += 1;
answer += lst[start]
for i in range(len(answer)):
    print(answer[i],end='')
    if (i+1)%80 == 0:print()


# https://www.acmicpc.net/problem/6137
# 걍 투포인터임