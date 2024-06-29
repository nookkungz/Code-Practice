n = int(input(""))
name = []
age = []
sex = []
for i in range(n):
    name1 = str(input(""))
    name.append(name1)
    age1 = int(input(""))
    age.append(age1)
    sex1 = str(input(""))
    sex.append(sex1)
print("--Customers Information--")
for i in range(0,n):
    print(f"{(name[i])} (age : {2017-(age[i])})")