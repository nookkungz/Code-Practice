ans = str(input(""))
done = ans
ansd = []
for i in ans :
    ansd.append(i)
    

pid = []

while True :
    n = str(input(""))
    if n == "0" :
        break
    pid.append(n)


point = 0
for i in range(len(ansd)) :
    if ansd[i] in pid :
        point += 1
        ansd[i] = []


    
print(f"{point}/{len(ans)}")
    
