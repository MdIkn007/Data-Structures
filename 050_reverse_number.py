s = input().strip()
rev = s[::-1] if not s.startswith('-') else '-' + s[:0:-1]
print(int(rev))
