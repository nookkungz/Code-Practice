def accum_sum(b) :
    for i in range(len(b)) :
        print(b[0])
        if len(b) == 1 :
            break
        done = b[0] + b[1]
        allsum = done
        b.pop(0)
        b[0] = allsum
    return
b = []
while True :
    n = int(input("Enter a number (0 to end): "))
    if n == 0 :
        break
    if n < 0 or n > 999 :
        print("Number is out of range.")
    else :
        b.append(n)
print("Original list:")
print(b)
print("Accumulative Sum:")
accum_sum(b)



