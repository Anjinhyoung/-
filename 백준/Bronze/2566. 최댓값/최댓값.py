List = []
for _ in range(9):
    a = list(map(int,input().split()))
    List.append(a)

Max = 0
row, column = 0,0

for i in range(9):
    for j in range(9):
        if Max <= List[i][j]:
            Max = List[i][j]
            row,column = i,j

print(Max)
print(row+1,column+1)