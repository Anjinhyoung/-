while True:
    try:
        a = int(input())
    except:
        break
    b = 1
    while True:
        if b % a != 0:
            b = b * 10 + 1
        else:
            print(len(str(b)))
            break