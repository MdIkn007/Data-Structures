ch = input().lower()
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Invalid")
