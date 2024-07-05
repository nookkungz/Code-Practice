box = [1,0,0]
n = str(input(""))
temp = []
for i in n :
    if i == "A" :
        temp = box[1]
        box[1] = box[0]
        box[0] = temp
    elif i == "B" :
        temp = box[2]
        box[2] = box[1]
        box[1] = temp
    elif i == "C" :
        temp = box[2]
        box[2] = box[0]
        box[0] = temp
for i in range (0,3,1) :
    if box[i] == 1 :
        print(i+1)

        
