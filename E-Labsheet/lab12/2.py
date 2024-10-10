input_string = input("Enter your string: ")

result = '"'
in_quotes = True

for i, char in enumerate(input_string):
    if char == ',':
        if in_quotes:
            result += '",'
        result += '"'
        in_quotes = True
    elif char == ' ':
        if i > 0 and input_string[i-1] != ',' and (i == len(input_string) - 1 or input_string[i+1] != ','):
            result += char
    else:
        result += char

if in_quotes:
    result += '"'

if input_string and input_string[-1] == ',':
    result += ',""'

# Print the result
print(result)