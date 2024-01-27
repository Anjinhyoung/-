def a(x):
    for i in range(2,x):
        if x%i == 0:
            return -1
    return 3

a1=int(input())
a2=list(map(int,input().split()))
cnt=0
for i in a2:
    if i==1:
        continue
    if a(i)==3:
        cnt+=1
print(cnt)