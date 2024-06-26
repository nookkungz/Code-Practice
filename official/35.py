pasw1 = str(input(""))
pasw = [str(x) for x in str(pasw1)]
pup , plow , pnum , psyn ,pcha , point = 0,0,0,0,0,0
if len(pasw) > 0 and len(pasw) < 21:
    for i in pasw :
        if i.upper() :
            pup += 1
        if i.lower() :
            plow += 1
        if i.isalnum() :
            pcha += 1
        if i.isdigit():
            pnum += 1
        if i.isalpha():
            psyn += 1
if pup > 0 :
    point += 1
if plow > 0: 
    point += 1
if pcha > 2 and pcha < 21 :
    point += 1
if pnum > 0 :
    point += 1 
if psyn > 0 :
    point += 1
if point > 4 :
    print("Valid")
else :
    print("Invalid")
print(pup)
print(pcha)
print(pnum)
print(psyn)
print(point)