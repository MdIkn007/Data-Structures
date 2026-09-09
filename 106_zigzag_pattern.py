cols = int(input())
for r in range(1, 4):
    for c in range(1, cols + 1):
        if (r + c) % 4 == 0 or (r == 2 and c % 4 == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
