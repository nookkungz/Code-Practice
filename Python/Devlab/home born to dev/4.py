n = int(input(""))
c = 0
p = 0
if n % 3 == 0:
    p = 1
if n % 2 == 0:
    c = 1
if p + c == 2:
    print("FizzBuzz")
elif p == 1:
    print("Fizz")
elif c == 1:
    print("Buzz")