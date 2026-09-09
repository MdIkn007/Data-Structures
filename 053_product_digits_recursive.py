def prod_digits(n):
    return n if n < 10 else (n % 10) * prod_digits(n // 10)
print(prod_digits(abs(int(input()))))
