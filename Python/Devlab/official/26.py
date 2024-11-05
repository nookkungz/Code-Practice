num = int(input(""))
if num > 100 :
    print("Error : Value must be less than or equal to 100.")
elif num > 89 and num < 101 :
    print("A")
elif num > 84 :
    print("B+")
elif num > 79 :
    print("B")
elif num > 74 :
    print("C+")
elif num > 69 :
    print("C")
elif num > 64 :
    print("D+")
elif num > 59 :
    print("D")
elif num < 60 and num >= 0 :
    print ("F")
else:
    print("Error : Value must be greater than or equal to 0.")