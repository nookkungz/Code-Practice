
hours = int(input('Enter number of hours: '))
minutes = int(input('Enter number of minutes: '))
buyAmt = int(input('Enter shopping amount: '))

cost = 0
while True :
    if hours >= 0 and hours <= 20 and minutes >= 0 and minutes <= 59 and (hours > 0 or minutes > 0) :
        time = ((hours*60)+minutes)/60
        if time > int(f"{time:.0f}") :
            time +=  1
            time = int(f"{time:.0f}")
            #print(cost , "1")
        time = int(f"{time:.0f}")
            #print(time)
        if time >= 0 and time <= 20 :
            if buyAmt >= 3001 :
                print("No charge, thank you.")
                break
            else :
                if time >= 2 :
                    time -= 2
                    #print(cost , "2")
                    if buyAmt >= 300 and buyAmt <= 3000 :
                        time -= 2
                        cost += 0
                        #print(cost , "3")
                    else :
                        if time >= 1 :
                            time -= 1 
                            cost += 20
                            #print(cost , "4")
                        if time >= 1 :
                            time -= 1 
                            cost += 20 
                            #print(cost , "5")
                    if time >= 1 :
                        cost += time*50
                        #print(cost , "6")
                    print(f"Total amount due is {cost} Baht, thank you.")
                    break
                else :
                    print("No charge, thank you.")
                    break
        else :
            print("Invalid time.")
            break
    else :
        print("Invalid time.")
        break
