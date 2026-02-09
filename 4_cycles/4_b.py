num = 0
while (sentences := input()) != "Приехали!":
    if "зайка" in sentences:
        num += 1
print(num)
