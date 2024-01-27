a = int(input())
b = list(map(int,input().split()))
c = True
for i in b:
    if (max(b) * min(b)) % i != 0:
        c = False
if c:
    print(max(b) * min(b))