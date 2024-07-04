g = [int (z) for z in input().split()]
x1 , s = g[0] , g[1]
i = 0
for i in range (-1000 , 1000 , 1) :
    if (x1 + i)/2 == s:
        print(i)
        break  
