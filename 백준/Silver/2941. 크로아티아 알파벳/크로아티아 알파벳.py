a = input()
b = ['c=','c-','dz=','z=','d-','lj','nj','s=']
for i in b:
    if i in a:
        a = a.replace(i,'a')
print(len(a))