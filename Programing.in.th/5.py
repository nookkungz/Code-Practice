x1 , x2 = map(int , input().split())
while x2 != 0:
    temp = x2
    x2 = x1 % x2
    x1 = temp
print(x1)

        