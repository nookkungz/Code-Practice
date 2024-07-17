h = int(input("Enter number of hours: "))
m = int(input("Enter number of minutes: "))
timer = (h*60 + m)
price = 0
if timer <= 15:
    price("No charge, thanks.")
else:
    timer -= 120
    price += 10
    if timer >= 1 :
        new = (timer // 60)
        price += (new*10)
        if timer % 60 > 0:
            price += 10
            print(f"Total amount due is {price} Bahts.")
    else :
        print(f"Total amount due is {price} Bahts.")
    