n = int(input(""))
all = []
for i in range (n):
    a = int(input(""))
    all.append(a)
avr = (sum(all)/n)
c = 0
for j in all :
    if j <= avr :
        c += 1
print(avr)
print("done",c)

