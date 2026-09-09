r, c = map(int, input().split())
for i in range(r):
    if i == 0 or i == r - 1:
        print("* " * c)
    else:
        print("*" + " " * (2 * c - 3) + "*")
