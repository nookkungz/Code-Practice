n = str(input(""))
c = str(input(""))
cl = []
for i in c :
    cl.append(i)


point = 0

for i in range (0,len(c)-2) :
    for j in n :
        print(j,"test")
        print(cl[i],"Check")
        if str(j) == str([cl[i]]) :
            point += 1
print(point)