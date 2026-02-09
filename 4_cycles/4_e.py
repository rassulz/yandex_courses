sum = 0
while (good := float(input())) != 0:
    if good >= 500:
        sum = sum + good * 0.9
    else: 
        sum = sum + good
print(sum)