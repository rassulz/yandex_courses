left = 1
right = 1000
attemps = 0

while attemps != 10:
    mid = (left + right) // 2
    print(mid)
    attemps += 1
    comments = input()

    if comments == "Больше":
        left = mid + 1
    elif comments == "Меньше":
        right = mid - 1
    else:
        break

