def digit(num):
    result = num%10
    return result
def tens(num) :
    result = num//10
    result = result%10
    return result
def hundreds(num) :
    result = num%1000
    result = result//10
    result = result//10
    return result
def thousands(num) :
    result = num//1000
    return result
def sum_digits(num) :
    result = thousands(num) + hundreds(num) + tens(num) + digit(num)
    return result

# main 
n   = int(input('Enter a number (0 to 9999): '))
print(f'Digit place is {digit(n)}.')
print(f'Tens place is {tens(n)}.')
print(f'Hundreds place is {hundreds(n)}.')
print(f'Thousands place is {thousands(n)}.')
print(f'Sum of all digits is {sum_digits(n)}.')