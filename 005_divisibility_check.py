n = int(input())
if n % 15 == 0:
    print("Divisible by both 3 and 5")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Divisible by neither")
