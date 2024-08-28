while True :
    n = int(input("Enter a number: "))
    if n == 0 :
        print("End of program, goodbye.")
        break
    elif n == 1 or n < 0 :
        print("Invalid input, try again.")
    else :
        j = 2
        c = 0
        while True :
            if n % j == 0 :
                c += 1
            j += 1
            if j == n+1 :
                break
        if c == 1 :
            print(f"{n} is a prime number.")
        else :
            print(f"{n} is not a prime number.")
        c = 0
        
    