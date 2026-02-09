start = int(input())
finish = int(input())

if start < finish:
    for number in range(start, finish + 1, 1):
        print(number, end=" ")
else:
    for number in range(start, finish - 1, -1):
        print(number, end=" ")
