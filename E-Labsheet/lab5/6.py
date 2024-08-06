n = int(input(""))
all = 0
while True :
        #print(n%10)
        all += n%10
        n = n //10
        if n == 0:
            break
if all%9 == 0 :
    print(f"Yes {all}")
else :
    print(f"No {all%9}")