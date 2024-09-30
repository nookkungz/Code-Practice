n = input("").strip()
nl = list(n)
point = 0
a = 0
count = 0
for char in nl:
    if char.isalpha():
        point = 1
        break
if point == 1:
    print("ERROR")
else:
    if "." in nl:
        decimal_index = nl.index(".")
        digits_after_decimal = len(nl) - decimal_index - 1
        if digits_after_decimal > 2:
            point = 2
    if point == 2:
        print("ERROR")
    else:
        if "." in nl:
            integer_part = n.split(".")[0]
        else:
            integer_part = n

        reversed_integer = integer_part[::-1]
        for i in range(len(reversed_integer)):
            if (i + 1) % 4 == 0:
                if reversed_integer[i] != ",":
                    point = 3
                    break
            else:
                if reversed_integer[i] == ",":
                    point = 3
                    break
        if point == 3:
            print("ERROR")
        else:
            cleaned_number = n.replace(",", "")
            if "." in cleaned_number:
                if cleaned_number.replace(".", "").isdigit():
                    result = float(cleaned_number)
                    print(result)
                else:
                    print("ERROR")
            else:
                if cleaned_number.isdigit():
                    result = int(cleaned_number)
                    print(result)
                else:
                    print("ERROR")
