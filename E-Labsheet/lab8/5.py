

def change (m,x) :
    c = 0
    if x == 500 :
        c = (m//500) 
        m = m - (c)*500
        return c
    elif x == 100 :
        c = (m//100)
        m = m - (c)*100
        return c
    elif x == 20 :
        c = (m//20)
        m = m - (c)*20
        return c
    elif x == 5 :
        c = (m//5)
        m = m - (c)*5
        return c
    return 0


money = int(input("Enter total money: "))
b500 = change(money,500)
left = money - (b500 * 500)
b100 = change(left , 100)
left = left - (b100 * 100)
b20 = change(left,20)
left = left - (b20 * 20)
b5 = change(left,5)
left = left - b5 * 5
b1 = left

print(f"500: {b500}")
print(f"100: {b100}")
print(f" 20: {b20}")
print(f"  5: {b5}")
print(f"  1: {b1}")