L = []
for _ in range(5):
    L.append(input())

for j in range(15):
    for i in range(5):
        if j < len(L[i]):
            print(L[i][j],end="")