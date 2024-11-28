num = int(input("Enter year: "))
if num > 400 :
    a = num%4
    if a == 0 :
        v = num%100
        if v > 1 :
            print(f"{num} is a leap year.")
        else :
            a = num%400
            if a == 0:
                print(f"{num} is a leap year.")
            else :
                print(f"{num} is not a leap year.")
    else :
        print(f"{num} is not a leap year.")
else :
    print("Invalid year.")
