a, b = map(int,input().split())
l = [0] * a

for i in range(b):
    c, d, e =map(int,input().split())
    l[c-1:d] = [e] * (d - c + 1)

for j in l:
    print(j, end=" ")