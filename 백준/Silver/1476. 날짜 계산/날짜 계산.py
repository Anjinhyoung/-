from sys import stdin
a,b,c = map(int,input().split()[:3])
year = 1
while True:
    if (year - a) % 15 == 0 and (year - b) % 28 == 0 and (year - c) % 19 == 0:
        print(year)
        break
    else:
        year += 1