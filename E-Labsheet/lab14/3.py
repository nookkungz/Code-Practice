variables = {}



print("Enter variables and values:")
while True :
    text = input()
    if text == '-1' :
        break
    [var , val] = text.split('=')
    var = var.strip()
    val = val.strip()
    variables[var] = val

lines = []
print("Enter your program:")
while True :
    text = input()
    if text == "-1" :
        break
    for var in variables:
        key = "{" + var + "}"
        text = text.replace(key,variables[var])
    lines.append(text)


print("Result:")
for line in lines :
    print(line)