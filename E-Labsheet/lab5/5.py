n = int(input("Enter height: "))
c , t = n , 0
while True :
    c -= 1
    if n == 0 :
        break
    if c < n-2 :
        t += 2
    if c == n-1 :
        print("  "*c , end= "")
        print("1")
    if c < n-1 :
        print("  "*c , end= "")
        print("1" + " "*t + "   " + " "*t + "1" )

    if c == 0 :
        break
    