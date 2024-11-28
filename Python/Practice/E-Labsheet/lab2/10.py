m = float(input("Enter buying amount: "))
if m >= 1000 and m < 3000 :
    m = (m*(100-10))/100 
    print(f"Amount due after discount is {m:.2f} baht.")
elif m >= 3000 :
    m = (m*(100-15))/100 
    print(f"Amount due after discount is {m:.2f} baht.")
else :
    print(f"Amount due after discount is {m:.2f} baht.")