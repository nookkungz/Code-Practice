# Input values
a = 3
b = 8
c = 9
d = 12

# Calculate the numerator and denominator of the result
numerator = a * d + c * b
denominator = b * d

# Simplify the fraction by finding the greatest common divisor (GCD)
x, y = numerator, denominator
while y:
    x, y = y, x % y
g = x

numerator //= g
denominator //= g

# Print the result
print(f"Summation of the two fractions is {numerator} / {denominator}")
