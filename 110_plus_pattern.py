n = int(input())
for i in range(n):
    print("*" * n if i == n // 2 else " " * (n // 2) + "*")
