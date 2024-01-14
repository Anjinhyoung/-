a, b = list(map(int,input().split()))
l = [i for i in range(1,a+1)]
for i in range(b):
    c,d = list(map(int,input().split()))
    l[c-1:d] = l[c-1:d][::-1]
print(*l)