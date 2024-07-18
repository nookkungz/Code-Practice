n = int(input("Enter your guess (0 - 100): "))
if n >= 0 and n <= 100 :
    if n == target :
        print("Congratulations, your guess is correct.")
    else:
        print("Sorry, your guess is wrong, try again later.")
else :
    print("Sorry, out of range, try again later.")