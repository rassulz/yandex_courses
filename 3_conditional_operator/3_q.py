import math

a = float(input())
b = float(input())
c = float(input())

if a != 0:
    d = (b ** 2) - 4 * a * c
    if d < 0:
        print("No solution")
    elif d == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
else:
    if b != 0:
        x = -c / b
        print(f"{x:.2f}")
    else:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
