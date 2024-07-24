t = int(input("How many TVs? "))
d = int(input("How many DVD players? "))
a = int(input("How many Audio Systems? "))
TV ,  DVD , AUDIO = 6000 , 1500 , 3000
total = (TV * t) + (DVD * d) + (AUDIO * a)
if total < 24000 :
    print(f"Your parment is {total:.2f} baht. Thank you!")
else : 
    print(f"Total price is {total:.2f} baht.")
    dis = total*0.2
    print(f"You've got a discount of {dis:.2f} baht.")
    print(f"Your payment is {(total - dis):.2f} baht. Thank you!")