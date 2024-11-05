n = str(input(""))
c = str(input(""))
cl = []
if n != "[]" :
    for i in c :
        cl.append(i)


    for i in range (0,len(cl)) :
        if i == len(cl)-1 :
            break
        if cl[i] == cl[i+1] :
            cl[i] = ""



    point = 0

    for j in cl :
        for i in n :
            if i == j :
                point += 1 

    print(point)
    print(f"{100/(len(n)-2)*point:.2f}")
else :
    print("0")
    print("0.00")