num = int(input())
cnt = 0
for i in range(0, num):
    sentences = input()
    if "зайка" in sentences:
        cnt += 1
print(cnt)