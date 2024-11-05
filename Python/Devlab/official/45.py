n = input()
store = []
temp = []
for c in range(len(n)):
    if n[c].isdigit():
        temp.append(n[c])
    else:
        if temp:
            store.append(int(''.join(temp))) 
            temp = []
if temp:
    store.append(int(''.join(temp)))
print(f"{sum(store):04d}")
