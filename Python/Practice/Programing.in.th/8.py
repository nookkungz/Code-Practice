
all = []
for i in range(5):
    n1 = sum([int(z) for z in input().split(" ")])
    all.append(n1)
winer = max(all)
for i in range(1,6):
    if all[i-1] == winer:
        print(i , winer)

