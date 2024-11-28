scores = []
done = [0,0,0,0,0,0,0,0,0,0,0]
c = 0
while len(scores) < 20 :
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
    else:
        scores.append(n)
if len(scores) == 20 :
    print("Original list:")
    print(scores)
    for i in range (0,11) :
        for j in scores :
            if j == i :
                done[i] += 1
    for i in done :
        t = "*"*i
        print(f"{c:>2} {t}")
        c += 1
