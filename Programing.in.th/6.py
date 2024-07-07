def gcd(x1, x2):
  """
  This function calculates the greatest common divisor (GCD) of two integers.
  """
  while x2 != 0:
    temp = x2
    x2 = x1 % x2
    x1 = temp
  return x1

# Get input from the user
x1, x2 = map(int, input().split())

# Calculate the GCD
gcd_value = gcd(x1, x2)

# Print the GCD
print(gcd_value)
