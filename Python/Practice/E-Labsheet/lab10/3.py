
def find_sd(scores) :
    lmean = sum(scores)/len(scores)
    lmeans = 0
    for i in scores :
        lmeans += (i-lmean)**2
    lmeans = lmeans/(len(scores)-1)
    done = lmeans**0.5
    return done

scores = []
while True :
    n = float(input("Enter score: "))
    if n == -1 :
        break
    if n < 0 or n > 100 :
        print("Score is out of range.")
    else :
        scores.append(n)

if scores :
    print(f"Maximum score is {max(scores):.2f}.")
    print(f"Minimum score is {min(scores):.2f}.")
    print(f"Average score is {(sum(scores)/len(scores)):.2f}.")
    print(f"Standard deviation is {find_sd(scores):.2f}.")
