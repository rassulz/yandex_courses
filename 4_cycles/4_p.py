num = int(input())

original_num = num

rever_num = 0

while num != 0:
    digit = num % 10
    rever_num = rever_num * 10 + digit
    num = num // 10
if original_num == rever_num:
    print("YES")
else:
    print("NO")