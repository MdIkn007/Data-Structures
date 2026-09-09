mode, val = input().split()
val = float(val)
if mode.upper() == 'C':
    print(f"{(val * 9/5) + 32:.2f} F")
else:
    print(f"{(val - 32) * 5/9:.2f} C")
