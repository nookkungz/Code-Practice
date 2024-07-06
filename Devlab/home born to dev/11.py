num = []
for i in range (10) :
    n = int(input())
    num.append(n%42)
print(num)
print(len(set(num)))

