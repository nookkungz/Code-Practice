print("First fraction:")
a = int(input("Enter a numerator a: "))
b = int(input("Enter a denominator b: "))
print("Second fraction:")
c = int(input("Enter a numerator c: "))
d = int(input("Enter a denominator d: "))

numerator = a * d + b * c
denominator = b * d

print(f"Summation of the two fractions is {numerator} / {denominator}")
