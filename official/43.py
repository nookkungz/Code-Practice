num = int(input(""))
y = 1
for i in range(num-1,0,-1):
    print(" "*i,end="")
    print("*"*y)
    y += 2
y = (num*2)-1
for i in range(0,num):
    print(" "*i,end="")
    print("*"*y)
    y -= 2