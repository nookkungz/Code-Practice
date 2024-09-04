

def check_prime (n) :
    c = n
    done = 0
    while True :
        if n%c == 0 :
            done += 1
        c -= 1
        if c == 0 :
            break
        
    if done == 2:
        return True
    else :
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")