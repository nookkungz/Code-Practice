def nb_year(p0 , percent , aug ,p ) :
    done = 0
    while True :
        p0 +=  int(p0*(percent/100)) + aug
        done += 1
        if p0 >= p :
            return done
    

print( nb_year(1000, 2, 30, 1150) )
print( nb_year(1500000, 0.25, 1000, 2000000) )