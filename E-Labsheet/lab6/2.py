c = 0
while True :
    guess = int(input("Enter your guess: "))
    c += 1
    if guess < 0 or guess > 100 :
        print("Sorry, your guess is out of range.")
    elif guess > 72 :
        print("Sorry, your guess is too high.")
    elif guess < 72 :
        print("Sorry, your guess is too low.")
    elif guess == 72 :
        print("Congratulations, your guess is correct.")
        print(f"Total number of guesses is {c}.")
        break

   
