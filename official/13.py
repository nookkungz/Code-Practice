x = int(input(""))
x2 = int(input(""))
if x > x2:
    max = x
    min = x2
elif x2 > x :
    max = x2 
    min = x
print(f"MAX : {max}")
print(f"MIN : {min}")