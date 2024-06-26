n = int(input(""))
c = int(input(""))
check = []
for i in range (c):
    ch = str(input(""))
    check = ch.split(" ")
    if n >= int(check[0]) and n <= int(check[1]) :
        print(check[2])
