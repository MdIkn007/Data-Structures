a, b, c = map(int, input().split())
if a + b > c and b + c > a and a + c > b:
    print("Valid")
else:
    print("Invalid")
