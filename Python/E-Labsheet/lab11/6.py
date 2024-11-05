n = str(input(""))
sala = ['a','e','i','o','u']
nl = []

for i in n :
    nl.append(i)

if len(nl) > 0 and len(nl) < 100 :
    for i in range (len(nl)) :
        if i == len(nl)-1 :
            break
        for j in sala :
            if nl[i] == j and n[i+1] == 'p' and n[i+2] == j:
                nl[i+1] , nl[i+2] = "" , ""

    done = ""
    for i in nl :
        if i != "" :
            done += i
    print(done)
else :
    print(n)