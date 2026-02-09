a = int(input())
max_digit = "яяяяяяяяя"

for i in range(a):
    name = input()
    if name < max_digit:
        max_digit = name

print(max_digit)
