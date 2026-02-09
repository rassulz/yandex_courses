a = int(input())
d = 2
first = True
while a > 1:
    if a % d == 0:
        if not first:
            print(" * ", end="")
        print(d, end="")
        first = False
        a //= d
    else:
        d += 1

