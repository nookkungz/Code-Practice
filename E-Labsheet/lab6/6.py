all = 0
target = int(input(""))
while True :
    all += (target%10)
    target = target //10
    if target == 0:
        if all >= 10 :
            target = all
            all = 0
        else :
            print(all)
            break