sen1 = input()
sen2 = input()
sen3 = input()

n1 = 0
n2 = 0
n3 = 0

n3 = len(sen3)
n1 = len(sen1)
n2 = len(sen2)

flag1 = 0
flag2 = 0
flag3 = 0

if "зайка" in sen1:
    flag1 = True
if "зайка" in sen2:
    flag2 = True
if "зайка" in sen3:
    flag3 = True


if flag1 == 1 and flag2 == 0 and flag3 == 0:
    print(sen1, n1)
elif flag1 == 0 and flag2 == 1 and flag3 == 0:
    print(sen2, n2)
elif flag1 == 0 and flag2 == 0 and flag3 == 1:
    print(sen3, n3)

elif flag1 == 1 and flag2 == 1 and flag3 == 0:
    if sen1 < sen2 and sen1 < sen2:
        print(sen1, n1)
    else:
        print(sen2, n2)
elif flag1 == 0 and flag2 == 1 and flag3 == 1:
    if sen2 < sen3 and sen2 < sen3:
        print(sen2, n2)
    else:
        print(sen3, n3)
elif flag1 == 1 and flag2 == 0 and flag3 == 1:
    if sen1 < sen3 and sen1 < sen3:
        print(sen1, n1)
    else:
        print(sen3, n3)    
elif flag1 == 1 and flag2 == 1 and flag3 == 1:
    if sen1 < sen2 and sen1 < sen3:
        print(sen1, n1)
    elif sen2 < sen1 and sen2 < sen3:
        print(sen2, n2)
    else:
        print(sen3, n3)

