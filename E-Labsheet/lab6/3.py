n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n11 = n1
n22 = n2
while True :
    mod = n1%n2
    n1 = n2 
    if mod == 0 :
        break
    n2 = mod 
while True :
    if n11 > n22:
       greater = n11
    else:
       greater = n22

    while(True):
       if((greater % n11 == 0) and (greater % n22 == 0)):
           lcm = greater
           break
       greater += 1
    break
print(f"  >> gcd({n11}, {n22}) ={n2:>7}")
print(f"  >> lcm({n11}, {n22}) ={lcm:>7}")
