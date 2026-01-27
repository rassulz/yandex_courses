a = int(input())
b = int(input())
c = int(input())

name1 = "Петя"
name2 = "Вася"
name3 = "Толя"

max_val = max(a, b, c)
min_val = min(a, b, c)
average_val = a + b + c - max_val - min_val


if a == max_val:
    print(f"          {name1}")
if b == max_val:
    print(f"          {name2}")
if c == max_val:
    print(f"          {name3}")

if a == average_val:
    print(f"  {name1}")
if b == average_val:
    print(f"  {name2}")
if c == average_val:
    print(f"  {name3}")

if a == min_val:
    print(f"                  {name1}")
if b == min_val:
    print(f"                  {name2}")
if c == min_val:
    print(f"                  {name3}")

print("   II      I      III")


