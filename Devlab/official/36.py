num = int(input(""))
x = 1
y = 2
r = num
for i in range(1,num+1,1):
    for j in range(y+1,1,-1) :
        print(" "*r , end="")
        print("*"*x)
        x += 2
        r -= 1
    x = 1
    y += 1
    r = num

print(" "*num + "|") 
print("="*num + "V" + "="*num)