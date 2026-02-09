n = int(input())

prev = 0  # предыдущий хэш

for index in range(n):
    block = int(input())

    h = block % 256
    r = (block // 256) % 256
    m = block // (256 * 256)

    calc_h = (37 * (m + r + prev)) % 256

    if h >= 100 or h != calc_h:
        print(index)
        break

    prev = h
else:
    print(-1)
