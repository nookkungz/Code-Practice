num = int(input(""))
total = []
for i in range(num):
    x = int(input(""))
    total.append(x)
total.sort(reverse=True)
for i in total:
    print(i)