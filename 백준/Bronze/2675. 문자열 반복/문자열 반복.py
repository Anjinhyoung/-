a = int(input())
for _ in range(a):
    b = input().split()
    for i in b[1]:
        print(i*int(b[0]),end="")
    print()