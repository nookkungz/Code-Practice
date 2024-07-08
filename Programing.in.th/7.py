Adrian = ""
Bruno = ""
Goran = ""


Adrianp , Brunop , Goranp = 0,0,0
n = int(input())
x = str(input())


for _ in range(0,n):
    Adrian += "ABC"
    Bruno += "BABC"
    Goran += "CCAABB"

for i in range (0,n,1) :
    if Adrian[i] == x[i] :
        Adrianp += 1
    if Bruno[i] == x[i] :
        Brunop += 1
    if Goran[i] == x[i] :
        Goranp += 1        
total = max(Adrianp , Brunop , Goranp)
print(total)
if Adrianp == total:
    print("Adrian")
if Brunop == total :
    print("Bruno")
if Goranp == total :
    print("Goran")
