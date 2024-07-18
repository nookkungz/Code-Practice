import math
x = float(input("Enter x : "))
if x < 0 :
    y = math.sqrt((x**2) + 1)
elif x == 0 :
    y = x
elif 0 < x <= 99 :
    y = (3*(x**2)) - (1-(x**2))
else :
    y = (2*(x**3)) - (x/(math.sqrt(x+1)))
print(f"f({x:.2f}) = {(math.ceil(y))}")