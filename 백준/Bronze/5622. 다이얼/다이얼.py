l = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
a = input()
count = 0
for i in a:
    for j in l:
        if i in j:
            count += l.index(j) + 3
print(count)