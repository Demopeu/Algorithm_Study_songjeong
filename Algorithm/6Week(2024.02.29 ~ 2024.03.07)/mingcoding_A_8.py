
import sys
input=sys.stdin.readline
def func(li,cnt,idx):
    global res
    if len(li)==1:
        res=max(res,cnt+li[0])
        return
    for i in range(idx,len(li)):
        if i==0:
            func(li[1:],cnt+li[1],max(0,i-1))
        elif i==len(li)-1:
            tmp=li.pop()
            func(li,cnt+li[-1],max(0,i-1))
            li.append(tmp)
        else:
            func(li[:i]+li[i+1:],cnt+li[i-1]*li[i+1],max(0,i-1))
for m in range(int(input())):
    N=int(input())
    li=list(map(int,input().split()))
    res=-1
    func(li,0,0)
    print(f'#{m+1}',res)

