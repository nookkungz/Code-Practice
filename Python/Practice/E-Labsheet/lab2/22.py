l = int(input("Enter level pokemon: "))
x = str(input("Enter level pokeball: "))
d = int(input("Enter distance: "))
x = x.lower()
if l >= 0 and l <= 40 :
    if x == "l":
        x = 0.05
    elif x == "m" :
        x = 0.03 
    elif x == "h" :
        x = 0.01
elif l >= 41 and l <= 60 :
    if x == "l":
        x = 0.03
    elif x == "m" :
        x = 0.05
    elif x == "h" :
        x = 0.01
if l >= 61 and l <= 100 :
    if x == "l":
        x = 0.1
    elif x == "m" :
        x = 0.08
    elif x == "h" :
        x = 0.01
s = 100 - (l*d*x)

if s >= 0 and s <= 100 :
    print(f"{s:.2f} percent.")
else :
    print(f"0.00 percent.")