scores = []
for i in range (20) :
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
        break
    scores.append(n)
if len(scores) == 20 :
    print(scores)