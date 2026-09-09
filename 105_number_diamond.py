n = int(input())
for i in range(1, n + 1):
    row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print("  " * (n - i) + " ".join(map(str, row)))
for i in range(n - 1, 0, -1):
    row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
    print("  " * (n - i) + " ".join(map(str, row)))
