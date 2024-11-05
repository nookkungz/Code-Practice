an = str(input(""))
ans = []
for i in an:
    ans.append(i)
gus = []
done = ["-"]*len(ans)
while True :
    g = str(input(""))
    if g == "0" :
        break
    gus.append(g)
for i in range (len(gus)) :
    for j in range(len(ans)) :
        if gus[i] == ans[j] :
            done[an.find(gus[i])] = ans[j]
            ans[j] = ""

for i in done :
    print(i , end = "")
            