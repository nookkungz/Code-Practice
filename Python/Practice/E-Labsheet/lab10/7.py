
exam = int(input(""))
exsesc = float(input(""))
nisit = int(input(""))
nisits = []

for i in range (nisit) :
    n = int(input(""))
    nisits.append(n)
c = 0
for i in nisits :
    if (i/exam)*100 < exsesc :
        c += 1
print(c)

for i in range(0,nisit) :
    if (nisits[i]/exam)*100 >= exsesc :
        print(f"{i+1} {(nisits[i]/exam)*100:.2f}")
    else :
        print(f"({i+1}) {(nisits[i]/exam)*100:.2f}")

