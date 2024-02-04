a,b = map(int,input().split())

l = [ [0] * b for _ in range(a) ]
l2 = [ [0] * b for _ in range(a) ]

for i in range(a):
    l[i] = list(map(int, input().split()[:b]))

for i in range(a):
    l2[i] = list(map(int, input().split()[:b]))

l3 = [ [0] * b for _ in range(a) ]

for i in range(a):
    for j in range(b):
        l3[i][j] = l2[i][j] + l[i][j]

for i in l3:
    print(*i)