n = int(input(""))
if n == 0 :
    print("1")
else:
    done = []
    for i in range(1,n+1):
        done.append(i)
    total = done[0]
    for i in range(0,n-1):
        total += (total * done[i])
    print(total)