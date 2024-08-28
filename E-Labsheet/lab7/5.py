h = int(input("Enter height: "))
w = int(input("Enter width: "))
count = 0
if h <= 0 or w <= 0 :
    print("Invalid input, program terminates.")
else :
    while True :
        
        if count % 2 == 0 :
            b = w
            while True :
                print("* " , end = "")
                b -= 1
                if b == 0 :
                    print()
                    break 
            
        elif count % 2 == 1 :
            b = w
            while True :
                print(" *" , end = "")
                b -= 1
                if b == 0 :
                    print()
                    break 
        count += 1 
        if count == h :
            break 