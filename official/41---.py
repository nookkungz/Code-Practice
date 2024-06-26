n = str(input(""))
l = []
for i in n:
    l.append(i)
print(l)

original_list = ['H', 'E', '4', '5', 'L', '3', '2', 'L', 'O', '4']
new_list = []

for i in range(len(original_list)):
    # Check if the current element and the next element are both digits
    if i < len(original_list) - 1 and original_list[i].isdigit() and original_list[i + 1].isdigit():
        # If they are, merge them into a single integer and append to the new list
        new_list.append(int(original_list[i] + original_list[i + 1]))
        # Skip the next element since we've already used it
        i += 1
    else:
        # If the current element is not part of a digit pair, simply append it to the new list
        new_list.append(original_list[i])

print(new_list)
