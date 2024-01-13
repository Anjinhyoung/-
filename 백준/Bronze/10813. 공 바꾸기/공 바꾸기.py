a,b = list(map(int,input().split()))
l = [i for i in range(1,a+1)]
for i in range(b):
    c, d = list(map(int,input().split()))
    c2 = l[d-1]
    d2 = l[c-1]
    l[c - 1] = c2
    l[d - 1] = d2
print(*l)