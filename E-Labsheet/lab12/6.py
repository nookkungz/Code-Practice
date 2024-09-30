n = str(input(""))
nl = []
for i in n :
    nl.append(i)

point = 0
a = 0
count = 0

for i in range (len(nl)) :
    if nl[i] in "abcdefghijklmnopqrstuvwsyz" :
        point = 1 
        break
print(nl)
if point == 1 :
    print("ERROR")
else :
    for i in range (len(nl)) :
        if nl[i] == "." : 
            for j in range (i+1,len(nl)) :
                a += 1
            if a > 2 :
                point = 2 

    if point == 2 :
        print("ERROR")
    else :
        if "." not in nl :
            for j in range (len(nl)-1,-1,-1):
                print(j , j%4 , n[j])
                print(count)
                count =+ 1
                if count%4 == 0 : 
                    if nl[j] != "," :
                        print("ERROR")
                        break

