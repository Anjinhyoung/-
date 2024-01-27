count = 0
for _ in range(int(input())):
    a = input()
    t = True
    for i in range(len(a)-1):
        if a[i] != a[i + 1]:
            if a[i] in a[i + 2:]: 
                t = False
    if t:
        count += 1
print(count)