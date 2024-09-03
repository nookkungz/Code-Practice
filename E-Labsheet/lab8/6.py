import math
def sqrt_n_times(x , n) :
    done = x
    while True :
        
        done = math.sqrt(done)


        n -= 1
        if n == 0 :
            break

    return done


x = float(input())
n = int(input())
print(sqrt_n_times(x, n) )