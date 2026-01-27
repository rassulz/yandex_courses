x = float(input())
y = float(input())

# Проверка: внутри ли острова
inside_island = x ** 2 + y ** 2 <= 100

# Проверка: внутри ли зоны зыбучих песков
in_quicksand = (
    4 * y >= (x + 1) ** 2 - 36 and
    y <= 5 and
    x ** 2 + y ** 2 <= 25 and
    3 * y <= 5 * x + 35
)

if not inside_island:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif in_quicksand:
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")
