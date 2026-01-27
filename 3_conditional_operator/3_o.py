a = input()
b = input()

max_value = min(int(a[0]), int(a[1]), int(b[0]), int(b[1]))
min_value = max(int(a[0]), int(a[1]), int(b[0]), int(b[1]))
ave_value = int(a[0] + a[1] + b[0] + b[1] - max_value - min_value)