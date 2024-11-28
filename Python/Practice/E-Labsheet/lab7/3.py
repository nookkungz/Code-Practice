n = int(input("Enter a number: "))
if n <= 0 or n > 26 :
    print("Invalid input, program terminates.")
else :
    i = 1
    while i <= n :
        done = ""
        j = 0 
        while j < i :
            ch = ord("A") + j
            done += (chr(ch))
            j += 1
        print(done)
        i+= 1    
    i = n-1
    while i >= 0 :
        j = 0
        while j < i :
            print(chr(ord("A") + j) , end = "")
            j += 1
        print()
        i-= 1
