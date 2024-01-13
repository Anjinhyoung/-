a = int(input())
for i in range(a):
    l = []
    a,b = list(input().split())
    for j in b:
        l.extend(j*int(a))
    print(*l,sep="")