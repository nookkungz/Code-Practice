n = str(input(""))
newn = ""
for i in range(len(n)) :
    if n[i] not in "AaEeIiOoUu" :
        newn += n[i]
print(newn)