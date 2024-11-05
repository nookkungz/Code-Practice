
def fibo(n) :
    if n == 1 :
        return 1
    elif n == 2:
        return 1 
    else :
        c = n-2
        done = 1
        n1 = 1
        while True :
            done = done + n1
            temp = done - n1
            n1 = temp
            c -= 1
            if c == 0 :
                break
        return done

n = int(input("Enter n: "))
print("fibo({0}) = {1} ".format(n , fibo(n)))