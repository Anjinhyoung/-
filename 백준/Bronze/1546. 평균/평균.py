a=int(input())
a1=list(map(int,input().split()))
a2=max(a1)
sum=0
for i in range(a):
    a3=a1[i]/a2*100
    sum+=a3
print(sum/a)