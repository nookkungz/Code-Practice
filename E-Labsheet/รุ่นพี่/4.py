n = int(input("Please input number: "))
temp = n 
re = 0

while True :
    re = (re*10)+(temp%10)
    temp = temp // 10
    if temp == 0 :
        break




    
if re == n :
    print("True")
else :
    print("False")
