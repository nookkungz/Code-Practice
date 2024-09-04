def alternating(n) :
    if n%2 == 0 :
        return (-1*int(n/2))
    else :
        return int(-1*(int(n-1)/2))+n


n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n , alternating(n)))