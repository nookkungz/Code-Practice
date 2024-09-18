n = int(input(""))
j = 1
for i in range (n,0,-1) :
    print("|",end="")
    print((" "*(i-1)),end= "")
    print("*"*j,end= "")
    print((" "*(i-1)),end= "")
    print("|",end="")
    j += 2
    print()

    