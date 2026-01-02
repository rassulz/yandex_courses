a = input()
b = input()

while len(a) < 3:
    a = "0" + a

while len(b) < 3:
    b = "0" + b

s3 = int(a[2]) + int(b[2])
s2 = int(a[1]) + int(b[1])
s1 = int(a[0]) + int(b[0])

ss = str(s1 % 10) + str(s2 % 10) + str(s3 % 10)

print(int(ss))
