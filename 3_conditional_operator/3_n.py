a = input()

a = sorted(a)

if int(a[0]) != 0:
    min_value = a[0] + a[1]
else:
    min_value = a[1] + a[0]

max_value = a[2] + a[1]

print(min_value, max_value)
