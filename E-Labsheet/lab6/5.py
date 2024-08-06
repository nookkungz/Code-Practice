see = 0
nhi = 0
while True :
    n = int(input(""))
    
    if n > nhi :
        nhi = n
        see += 1

    if n == -1 :
        break
print(see)