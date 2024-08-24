h = int(input("Enter height : "))
w = int(input("Enter width : "))
while True :
    
    if h % 2 == 0 :
        b = w
        while True :
            print("* " , end = "")
            b -= 1
            if b == 0 :
                print()
                break 
        
    elif h % 2 == 1 :
        b = w
        while True :
            print(" *" , end = "")
            b -= 1
            if b == 0 :
                print()
                break 
                
    print(h)
    h -= 1 
    if h == 0 :
        break 