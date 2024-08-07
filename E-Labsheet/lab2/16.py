target = 72
n = int(input("Enter your guess (0 - 100): "))
if target == n :
    print("Congratulations, your guess is correct.")
elif n > 100 or n < 0 :
    print("Sorry, out of range, try again later.")
elif n > target :
    print("Sorry, your guess is too high, try again later.")
else :
    print("Sorry, your guess is too low, try again later.")

