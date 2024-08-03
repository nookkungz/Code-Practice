n = int(input(""))
while True :
    if n <= 0 :
        print("ERROR")
        break
    else :
        print(n%10)
        n = n //10
        if n == 0:
            break
    