num = []
while True:
    n = int(input(""))
    if n == 0:
        break
    num.append(n)
a = str(input("").lower())
if a == "max":
    num.sort(reverse=True)
    for i in num:
        print(i , end=" ")
elif a == "min":
    num.sort(reverse=False)
    for i in num :
        print(i , end=" ")