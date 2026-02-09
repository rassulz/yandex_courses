x = 0
y = 0
while True:
    dirMap = input()
    if dirMap == "СТОП":
        break
    steps = int(input())

    if dirMap == "СЕВЕР":
        y += steps
    elif dirMap == "ЮГ":
        y -= steps
    elif dirMap == "ЗАПАД":
        x -= steps
    elif dirMap == "ВОСТОК":
        x += steps
print(y)
print(x)