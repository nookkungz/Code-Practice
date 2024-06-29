x = int(input(""))
z = 1
for i in range (x,0,-1):
    print(" "*(i-1) , end="")
    print("*"*z , end="")
    z += 2
    print("")