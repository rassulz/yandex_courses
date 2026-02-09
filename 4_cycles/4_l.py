a = input()
max = a[0]
if len(a) > 1:
    for i in range(0, len(a) - 1):
        if max < a[i + 1]:
            max = a[i + 1]
    print(max)
else:
    print(max)