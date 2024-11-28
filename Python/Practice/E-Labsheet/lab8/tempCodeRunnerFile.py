def f1 (a , b) :
    done = 0
    while True :
        if b >= a%10 :
            done += 1
        a = a //10
        if a == 0:
            break
    
    return done