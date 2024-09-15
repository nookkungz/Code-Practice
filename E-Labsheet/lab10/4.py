
def find_mode(s) :
    ten = [0,0,0,0,0,0,0,0,0,0,0]
    for j in s :
        for i in range (0,11) :
            if j == i :
                ten[i] += 1
    for i in range (0,11) :
        if ten[i] == max(ten) :
            print(i)

scores = []


while True :
    if len(scores) == 20 :
        break 
    n = int(input("Enter score: "))
    if n < 0 or n > 10 :
        print("Score is out of range.")
    else :
        scores.append(n)

print("-----")
print("Original list:")
print(scores)
print("Mode of scores:")
find_mode(scores)