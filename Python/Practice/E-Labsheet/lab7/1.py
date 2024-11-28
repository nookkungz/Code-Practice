n = int(input("Enter a number: "))
if n <= 0 or n > 20 :
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