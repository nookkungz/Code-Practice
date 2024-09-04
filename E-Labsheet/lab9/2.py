
def factor_count(n) :
    c = n
    count = 0
    while True :
        
        if n%c == 0 :
            count += 1
        c -= 1
        if c == 0:
            break 
        
    return count

n = int(input("Enter n: "))
c = factor_count(n)
print(c)
