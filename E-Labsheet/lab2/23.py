import math

x = int(input("Minutes before due: "))
t = float(input("Temperature: "))
c = str(input("Is it raining (y/n)? "))
c = c.lower()
a = x//1440
if (x/1440) - (x//1440) >= 0.5 :
    day = a + 1
else :
    day = a
print(f">>> {day:.0f} days before due.")
if day < 2:
    done = ">>> I will do the assignment."
elif day > 5:
    done = ">>> I will not do the assignment."
else : 
    if t > 40 :
        done = ">>> I will not do the assignment."
    elif t > 25 :
        if c == "y" :
            done =  ">>> I will not do the assignment."
        else :
            done = ">>> I will do the assignment."
    else :
        done = ">>> I will do the assignment."
print(done)
