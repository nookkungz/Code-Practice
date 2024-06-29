n = []
done = []
for i in range(5):
    y = int(input(""))
    n.append(y)
n.sort(reverse=True)
for i in n:
    print(i)