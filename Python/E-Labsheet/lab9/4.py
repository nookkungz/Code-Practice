def fac(n) :
    done = 1
    if n == 0 :
        return 1
    while True :
        done = done*n
        n -= 1
        if n == 0 :
            return done






n = int(input("Enter n: "))
print(f"{n}!","=",fac(n))