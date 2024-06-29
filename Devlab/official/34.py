num1 = int(input(""))
num = [int(x)for x in str(num1)]
total = 0
done = sum(num)
while done > 9:
    donenew = [int(z)for z in str(done)]
    done = sum(donenew)
print(done)