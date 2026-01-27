a = int(input())
b = int(input())
c = int(input())
first_name = 'Петя'
second_name = 'Вася'
third_name = 'Толя'

if a > b and a > c and b > c:
    print(f"1. {first_name}")
    print(f"2. {second_name}")
    print(f"3. {third_name}")
elif a > b and a > c and c > b:
    print(f"1. {first_name}")
    print(f"2. {third_name}")
    print(f"3. {second_name}")
elif b > c and b > a and a > c:
    print(f"1. {second_name}")
    print(f"2. {first_name}")
    print(f"3. {third_name}")
elif b > c and b > a and c > a:
    print(f"1. {second_name}")
    print(f"2. {third_name}")
    print(f"3. {first_name}")
elif c > b and c > a and b > a:
    print(f"1. {third_name}")
    print(f"2. {second_name}")
    print(f"3. {first_name}")
# elif c > b and c > a and a > b:
else:
    print(f"1. {third_name}")
    print(f"2. {first_name}")
    print(f"3. {second_name}")