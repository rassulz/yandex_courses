N = int(input())  # общий вес масса
M = int(input())  # общий руб за килограмм
K1 = int(input())  # рублей за килограмм
K2 = int(input())  # рублей за килограмм


# x * K1 + (N - x) * K2 = M * N
# x K1 + N K2 - x K2 = M N
# x (K1 - K2) + N K2 = M N
# X = (M N - N K2)/(K1 - K2)

x = (M * N - N * K2) / (K1 - K2)

y = N - x

print(int(x), int(y))