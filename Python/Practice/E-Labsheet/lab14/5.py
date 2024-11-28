
dic = {}


while True :
    n = input()
    if n == "end" :
        break
    [name , amount] = n.split()
    if name in dic :
        if dic[name][0] < amount :
            dic[name][0] = amount
            dic[name][1] += 1
    else :
        dic[name] = [amount,1]
dic = dic.sort()
print(dic)