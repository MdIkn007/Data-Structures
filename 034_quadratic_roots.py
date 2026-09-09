import cmath
a, b, c = map(float, input().split())
d = (b**2) - (4*a*c)
r1 = (-b - cmath.sqrt(d)) / (2*a)
r2 = (-b + cmath.sqrt(d)) / (2*a)
print(f"Roots: {r1}, {r2}")
