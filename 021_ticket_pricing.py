age = int(input())
if age < 5:
    print("Free")
elif age <= 12:
    print("$10")
elif age <= 60:
    print("$20")
else:
    print("$15")
