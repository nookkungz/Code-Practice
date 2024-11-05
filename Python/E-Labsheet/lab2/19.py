c = str(input("Enter your buffet choice: "))
if c == "Korean" or "Japanese" :
    d = str(input("Is today Wednesday (yes/no)? "))
    total = 0
    if c == "Korean" :
        total = 1500
        if d == "yes" :
            total = total-(total * 0.15)
            print(f"Your payment is {total} Baht.")
        else :
            print(f"Your payment is {total} Baht.")
    elif c == "Japanese" :
        total = 850
        if d == "yes" :
            total = total-(total * 0.15)
            print(f"Your payment is {total} Baht.")
        else :
            print(f"Your payment is {total} Baht.")
else :
    print(f"Sorry, there is no {c} buffet.")
        