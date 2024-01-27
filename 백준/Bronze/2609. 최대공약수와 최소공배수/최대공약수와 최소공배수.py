a, b = list(map(int,input().split()))
l = []
for i in range(1,10001):
    if a % i == 0 and b % i == 0:
        l.append(i)

print(max(l))
print(max(l) * (b // max(l)) * (a//max(l)))