numbers = []
result = []
while True :
    n = int(input(""))
    if n == -1 :
        break
    numbers.append(n)

temp = 0
for i in numbers :
    if i > temp :
        temp = i 
        result.append(temp)
print(result)