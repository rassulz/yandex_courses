a = int(input())
b = int(input())

name1 = "Петя"
name2 = "Вася"
name3 = "Толя"
name4 = "Гена"
name5 = "Дима" 

# петя 7, Вася 6 
# петя 6, вася 9, толя x - 2
# петя 6, вася 12, толя x - 2 - 5, гена y + 2
# петя 6 + N, вася 12 + M

if (a + 6) > (b + 12):
    print(name1)
else:
    print(name2)