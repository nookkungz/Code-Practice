d = int(input(""))
h = int(input(""))
m = int(input(""))
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
if h >= 12 and h <= 18 :
    if h == 18 and m >= 1 :
        time = "evening"
    else :
        time = "afternoon"
if h >= 18 and h <= 22 :
    if h == 22 and m >= 1 :
        time = "evening"
    else :
        time = "night"
if (h >= 22 and h <= 24) or (h >= 0 and h <= 4 ) :
     
print(time)