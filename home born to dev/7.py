n = str(input(""))
n1 = n.split(",")
print(n1)
la = []
for i in n1 :
    if (i % 7 == 0) and (i % 11 != 0):
        la.append(i)
print(la)
