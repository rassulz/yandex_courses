name = input()
num = int(input())

org = num

d = num % 10
num = int(num / 10)

c = num % 10
num = int(num / 10)

b = num % 10

print(f"Группа №{b}.")
print(f"{d}. {name}.")
print(f"Шкафчик: {org}.")
print(f"Кроватка: {c}.")