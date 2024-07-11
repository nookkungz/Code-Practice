import math
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

print(f"a1 = {(x**y)+z:.2f}")
print(f"a2 = {(math.cos(2*math.pi)) + (math.log(x , math.e)):.2f}")
print(f"a3 = {abs(x)+abs(y):.2f}")
print(f"a4 = {(math.sqrt((x**2)+(y**2)+(z**2))):.2f}")
print(f"a5 = {x/y:.2f}")
print(f"a6 = {math.pow(x + y, 1/5):.2f}")
print(f"a7 = {math.exp(x * math.log(y)):.2f}")

