n = str(input(""))
total = 0
for i in n :
    if i in "AaEeIiOoUu" :
        total += 1
print(total)