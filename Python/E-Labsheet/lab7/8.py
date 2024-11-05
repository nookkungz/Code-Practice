c = int(input(""))

count = 0
a = 1
while a < c:
    b = a + 1
    while b < c:
        if a * a + b * b == c * c:
            count += 1
        b += 1
    a += 1

print(count)
