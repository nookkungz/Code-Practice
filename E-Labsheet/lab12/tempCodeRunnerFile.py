n = input()  
done = ""    
ins = False  

for i in range(len(n)):
    if n[i] != " " and n[i] != ",":
        if not ins:  
            done += '"'     
            ins = True
        done += n[i]        
    elif n[i] == ",":  
        if ins:  
            done += '"'
            ins = False
        done += ','  
    elif n[i] == " " and ins:  
        done += n[i]

if ins:
    done += '"'

if n[-1] == ",":
    done += ',""'

print(done)