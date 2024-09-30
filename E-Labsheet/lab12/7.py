camel = "-_=.$"
n = str(input(""))
nl = []
for i in n :
    nl.append(i)

for i in camel :
    for j in range (len(nl)) :
        if nl[j] == i :
            if j == 0:
                nl[j] = ""
                nl[j+1] = nl[j+1].upper()
            else :
                nl[j] = ""
                nl[j-1] = nl[j-1].lower()
                nl[j+1] = nl[j+1].upper()

for i in nl :
    print(i,end="")