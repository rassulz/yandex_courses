a = int(input())
b = int(input())
c = int(input())

min_value = min(a, b, c)
max_value = max(a, b, c)
average_value = a + b + c - min_value - max_value


if a == b and a == c: 
    print('YES')
elif max_value ** 2 == (min_value ** 2 + average_value ** 2):
    print("YES")
else:
    print("NO")