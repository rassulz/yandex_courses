number = int(input())

if number == 1:
    print("NO")
else:
    d = 2
    is_prime = True

    while d * d <= number:
        if number % d == 0:
            is_prime = False
            break
        d += 1

    if is_prime:
        print("YES")
    else:
        print("NO")
