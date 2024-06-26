n = int(input(""))
done = 0
z = [int(z) for z in input ("").split()]
find = int(input(""))
for i in z:
    if i == find :
        print("Yes")
        done = 1
if done == 0:
    print("No")
    
