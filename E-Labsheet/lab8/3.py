import math


def simple_interest(p , r , t) :
    result = p *(r/100) * t
    return result


def compound_interest(p, r, t) :
    return 0

#main
p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

print('Return money for simple interest calculation is {:.2f} Baht.'.format(simple_interest(p, r, t)))
print('Return money for compound interest calculation is {:.2f} Baht.'.format(compound_interest(p, r, t)))