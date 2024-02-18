a,b = map(int,input().split())
c, d = [],[]

for _ in range(a):
    a2 = list(map(int,input().split()))
    c.append(a2)

for _ in range(a):
    a2 = list(map(int,input().split()))
    d.append(a2)

for i in range(a):
    for j in range(b):
        print(c[i][j] + d[i][j], end=" ")
    print()