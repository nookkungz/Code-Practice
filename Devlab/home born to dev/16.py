n = str(input())
b = []
for i in n :
    if i.isupper():
        b.append(i.lower())
    elif i.islower():
        b.append(i.upper())
    else :
        b.append(i)
for i in b : print(i , end= "")
    