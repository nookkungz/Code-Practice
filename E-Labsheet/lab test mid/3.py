d = int(input(""))
h = int(input(""))
m = int(input(""))
print(m)
if d == 1 :
    day = "sunday"
elif d == 2 :
    day = "monday"
elif d == 3 :
    day = ""
elif d == 4 :
    day = ""
elif d == 5 :
    day = ""
elif d == 6 :
    day = ""
elif d == 7 :
    day = ""
if h >= 4 and h <= 12 :
    if h == 12 and m >= 1:
        time = "afternoon"
    else :
        time = "morning"
print(time)