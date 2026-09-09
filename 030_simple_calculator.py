a, op, b = input().split()
a, b = float(a), float(b)
ops = {'+': a + b, '-': a - b, '*': a * b, '/': (a / b if b != 0 else "Error: Div by 0")}
print(ops.get(op, "Invalid Operator"))
