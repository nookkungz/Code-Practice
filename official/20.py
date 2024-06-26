x = int(input(""))
if x > 1:
    print("#"*x)
    for i in range (x-2):
        print("#"+" "*(x-2) + "#")
    print("#"*x)
else:
    print("#")