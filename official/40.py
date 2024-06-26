x = str(input(""))
newx = ""
char = "aeiouAEIOU"
for i in x :
    if i in char :
        newx = newx
    else :
        newx += i
print(newx)