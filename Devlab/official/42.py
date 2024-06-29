num = int(input(""))
box = []
save = []
text = ""
x = 0
for i in range(num):
    box1 = int(input(""))
    box.append(box1)
find = int(input(""))
for i in box :
    x += 1
    if find == i :
        save.append(x)
if len(save) == 0:
    print("Not Found")
else :
    nsave = [str(num1)for num1 in save]
    for i in nsave:
        text += i
        text += ","
    ntext = text[:-1]
    print(f"Position: {ntext}")
        
