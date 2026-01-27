a = input()
b = input()
c = input()

if ord(a[0]) < ord(b[0]) and ord(a[0]) < ord(c[0]):
    print(a)
elif ord(b[0]) < ord(a[0]) and ord(b[0]) < ord(c[0]):
    print(b)
else:
    print(c)