n = int(input("Enter positive integer: "))

if n < 1:
    print("Invalid number.")
elif n == 1 :
    n = n
else:
    
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            print(factor)
            n //= factor
        factor += 1
