
n = int(input())


ls = []
for _ in range(n):
    ls.append(int(input()))

ls.sort(reverse=True)

amount = int(input())

donec = [0] * n
for i, de in enumerate(ls):
    if amount >= de:
        count = amount // de
        donec[i] = count
        amount -= count * de

for i, de in enumerate(ls):
    if donec[i] > 0:
        print(f"{de}: {donec[i]}")