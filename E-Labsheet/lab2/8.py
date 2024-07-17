c = float(input())
char = str(input())
output = 0
char = char.lower()
if char == "f"  :
    print(((9/5)*c) + 32)
elif char == "k" :
    print(c + 273.15)    
else :
    print("ERROR")
