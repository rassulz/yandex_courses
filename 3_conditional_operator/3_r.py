a = int(input())
b = int(input())
c = int(input())

a, b, c = sorted([a, b, c])

if a * a + b * b == c * c:
    print("100%")
elif a * a + b * b > c * c:
    print("крайне мала")
else:
    print("велика")