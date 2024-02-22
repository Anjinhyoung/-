
import sys
a1=[[0]*100 for i in range(100)]
a2=int(sys.stdin.readline())
cnt=0
for _ in range(a2):
    a,b=map(int,sys.stdin.readline().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            a1[i][j]=1
for i in a1:
    for j in i:
        if j==1:
            cnt+=1
print(cnt)
