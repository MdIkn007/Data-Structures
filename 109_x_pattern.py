n = int(input())
for i in range(n):
    for j in range(n):
        print("*" if j == i or j == n - 1 - i else " ", end="")
    print()
