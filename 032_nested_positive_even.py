n = int(input())
if n > 0:
    print("Positive and", "Even" if n % 2 == 0 else "Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
