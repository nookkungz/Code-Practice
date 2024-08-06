target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
storeg , storet= guess , target
point1 , point2 = 0 , 0
while True :
    #print(target%10)
    while True :
        if (guess%10 == target%10) :
            point1 += 1
        guess = guess // 10 
        if guess == 0 :
            guess = storeg 
            break
    target = target //10
    if target == 0:
        break
target = storet
guess = storeg
while True :
    #print(target%10)
    #print(guess%10)
    if target%10 == guess%10 :
        point2 += 1
    guess = guess // 10 
    target = target // 10 
    if target == 0 :
        break
while True :    
    point1 = (point1 - point2)
    point2 = (point2)
    if point1 == 1 :
        point1done = f"one digit correct"
    elif point1 == 2 :
        point1done = f"two digits correct"
    elif point1 == 3 :
        point1done = f"three digits correct"
    elif point1 == 4 :
        point1done = f"four digits correct"
    elif point1 == 0 :
        point1done = f"no digits correct"
    if point2 == 0 :
        point2done = f"No positions correct,"
    elif point2 == 1:
        point2done = f"One position correct,"
    elif point2 == 2:
        point2done = f"Two positions correct,"
    elif point2 == 3:
        point2done = f"Three positions correct,"
    elif point2 == 4:
        print("Congratulations, you just mastered my mind!!")
        break
    print(f"{point2done} {point1done}")
    break