n = str(input())
done = ""
sala = "aAeEIiOoUu"
for i in n :
    if i in sala :
        done += i.upper()
    elif i.islower() or i.isupper() :
        done += i.lower()
    else :
        done += i
print(done)
        