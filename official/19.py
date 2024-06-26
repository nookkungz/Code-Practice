num = int(input(""))
a = num%4
if a == 0 :
    v = num%100
    if v > 1 :
        print("Leap Year")
    else :
        a = num%400
        if a == 0:
            print("Leap Year")
        else :
            print("Not a Leap Year")
else :
    print("Not a Leap Year")
