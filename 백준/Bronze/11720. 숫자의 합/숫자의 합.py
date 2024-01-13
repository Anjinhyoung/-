a = int(input())
a2 = input()[:a]
b = list(map(lambda x:int(x),a2))
sum = 0
for i in b:
    sum += i
print(sum)