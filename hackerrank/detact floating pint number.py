n = int(input(""))
a = []
p , p2 = 0 , 0
for i in range(n):
    g = str(input(""))
    if (g[0] == "+" or g[0] == "-") and (g[1] != "+" or g[1] != "-"):
        for j in g:
            if j == ".":
                p += 1
            if j.isdigit():
                p2 += 1
        if p > 0 and p2 > 0 :
            print("True")
        else:
            print("False")
    else:
        print("False")