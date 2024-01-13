a = int(input())
for i in range(a):
    b = input()
    if len(b) == 1:
        print(b+b)
    else:
        print(b[0]+b[-1])