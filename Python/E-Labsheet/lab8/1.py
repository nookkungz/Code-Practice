import math
def circle (r)  :
    result = math.pi * r * r
    return result
 
def circumference(r) :
    result = 2 * math.pi * r
    return result

def sphere (r) :
    result = 4/3 * math.pi * r ** 3 
    return result



# main 


r = float(input("Enter a radius: "))

print('Area of a circle with radius {:.2f} is {:.2f}.'.format(r, circle(r)))
print('Circumference of a circle with radius {:.2f} is {:.2f}.'.format(r, circumference(r)))
print('Volume of sphere with radius {:.2f} is {:.2f}.'.format(r, sphere(r)))