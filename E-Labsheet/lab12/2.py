n = str(input(""))
done = ""
done += f'"'
for i in range (len(n)) :
    if i == len(n)-1 :
        done += f'{n[i]}"'
        break
    if n[i] == " " and ((n[i+1] == " " or n[i+1] == "," ) and (n[i-1] == ",")) :
        pass
    else:
        done += n[i]
    if n[i+1] == "," :
        done += f'"'
    if n[i] == ",":
        done += f'"'
if n[-1] == "," :
    done += f',""'
print(done)