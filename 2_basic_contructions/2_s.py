product = input()
price = int(input())
weight = int(input())
money = int(input())

total = price * weight
change = money - total

print(f"{'Чек':=^35}")
print(f"{'Товар:':<10}{product:>25}")
print(f"{'Цена:':<10}{f'{weight}кг * {price}руб/кг':>25}")
print(f"{'Итого:':<10}{f'{total}руб':>25}")
print(f"{'Внесено:':<10}{f'{money}руб':>25}")
print(f"{'Сдача:':<10}{f'{change}руб':>25}")
print("=" * 35)
