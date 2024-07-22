n1 = int(input())
n2 = int(input())
c = 0
for i in range (n1,n2+1):
    for j in str(i) :
        if j == "9" :
            c += 1
print(c)
