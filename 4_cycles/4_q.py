a = int(input())
org_a = a
updated = 0
multiplier = 1  # для восстановления порядка

while a != 0:
    digit = a % 10
    if digit % 2 != 0:
        updated += digit * multiplier
        multiplier *= 10
    a = a // 10

print(updated)