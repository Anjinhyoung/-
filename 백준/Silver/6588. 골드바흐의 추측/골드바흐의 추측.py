from sys import stdin

a = [True] * 1000001
a[0] = a[1] = False
for i in range(2,1001):
    if a[i]:
        for j in range(i+i,1000001,i):
            a[j] = False

while True:
    sum = 0
    b = int(stdin.readline())
    if b == 0:
        break
    for j in range(3,b+1):
        if a[j] and a[b-j]:
            print(f"{b} = {j} + {b-j}")
            sum +=1
            break
    else:
        print("Goldbach's conjecture is wrong.")
        sum+=1
    if sum == 1000000:
        break