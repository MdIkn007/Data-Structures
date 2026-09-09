n = int(input())
for i in range(1, n + 1):
    print(*(chr(65 + j) for j in range(i)))
