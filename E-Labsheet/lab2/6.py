x = float(input())
y = float(input())
z = float(input())

# a1
print(f"a1 = {(x**y)+z}")

# a2 (since cos(2*pi) is always 1)
print(f"a2 = {(1) + (math.log(x))}")  # Note: math.log is still needed

# a3
print(f"a3 = {abs(x)+abs(y)}")

# a4
print(f"a4 = {(x**2 + y**2 + z**2)**0.5}")  # Use pow instead of math.sqrt

# a5 (due to trigonometric identity)
print(f"a5 = {x**2 + (1 - x**2)}")  # Leverage sin^2(x) + cos^2(x) = 1

# a6
print(f"a6 = {(5 * (x + y))**0.5}")  # Use pow instead of math.sqrt

# a7
print(f"a7 = {pow(2.71828, x * math.log(y))} ")  # Use a constant for e