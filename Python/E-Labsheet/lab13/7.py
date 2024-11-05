numbers = []

while True:
    num_input = input("Enter a number (-1 to end): ")
    
    if num_input == "-1":
        break
        
    if num_input.isdigit() or (num_input[0] == '-' and num_input[1:].isdigit()):
        num = int(num_input)
        if 0 <= num <= 100:
            numbers.append(num)
        else:
            print("Number is out of range.")
    else:
        print("Please enter a valid integer.")

print("-----")
print("Original list:")
print(numbers)

if not numbers:
    print("The list is empty.")
else:
    is_non_increasing = True
    is_non_decreasing = True

    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            is_non_increasing = False
        if numbers[i] > numbers[i + 1]:
            is_non_decreasing = False

    if is_non_increasing and is_non_decreasing:
        print("The list is in non-increasing and non-decreasing order.")
    elif is_non_increasing:
        print("The list is in non-increasing order.")
    elif is_non_decreasing:
        print("The list is in non-decreasing order.")
    else:
        print("The list is in random order.")