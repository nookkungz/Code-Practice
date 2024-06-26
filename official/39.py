x = str(input(""))
newx = ""
for i in x :
    if i.isupper():
        newx += i.lower()
    elif i.islower ():
        newx += i.upper()
    else:
        newx += i
print(newx)