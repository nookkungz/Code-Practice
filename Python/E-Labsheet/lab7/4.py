n = int(input("Enter a number: "))
if n < 0 :
    print("Invalid input, program terminates.")
else :
    j = 0
    x = n
    done = 1
    temp = ""
    while True :
        print(f"{j}! = " , end = "")
        if n == 0 :
            print(f"1 = 1")
        elif j == 0  or j == 1:
            print("1 = 1")
        else :
            x = j
            while x > 0 :
                done *= x
                temp += str(x)
                if x > 1 :
                    temp += " x "
                x -= 1
            print(f"{temp} = {done}")
            temp = ""            
            done = 1
        j += 1
        if j == n + 1 : break