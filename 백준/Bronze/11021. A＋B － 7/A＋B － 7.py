import sys
a = sys.stdin.readline().strip()
for i in range(1,int(a)+1):
    b,c = sys.stdin.readline().strip().split()
    print(f"Case #{i}:",int(b)+int(c))