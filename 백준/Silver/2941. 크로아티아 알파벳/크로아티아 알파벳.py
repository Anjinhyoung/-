a = ['dz=','z=','c=','c-','s=','d-','lj','nj']
b = input()
for i in a:
    if i in b:
        b = b.replace(i,"a")
print(len(b))