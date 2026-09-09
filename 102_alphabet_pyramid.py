n = int(input())
for i in range(1, n + 1):
    chars = [chr(65 + j) for j in range(i)]
    chars += chars[-2::-1]
    print(" " * (n - i) + "".join(chars))
