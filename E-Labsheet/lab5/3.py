c = 0
while True :
    n = int(input("Enter number: "))
    if n < 0 :
        break 
    if n%2 > 0 :
        c += 1 
print(f"Received {c} odd numbers")