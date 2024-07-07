n = []
for i in range (0,9,1) :
    temp = int(input())
    n.append(temp)
done = False
for i in range (0,9,1):
    for j in range(0,9,1):
        if (sum(n) - n[i] - n[j]) == 100 :
            n.pop(i)
            n.pop(j-1)
            done = True
            break
    if done :
        break
            
for i in n : print(i)