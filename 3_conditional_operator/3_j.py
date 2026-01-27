a = input()

num1 = int(a[2]) + int(a[1])
num2 = int(a[0]) + int(a[1])

if num1 > num2:
    print(int(str(num1) + str(num2)))
else:
    print(int(str(num2) + str(num1)))   