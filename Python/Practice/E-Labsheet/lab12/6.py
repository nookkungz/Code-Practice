def format_number(input_str):
    # Remove leading/trailing whitespace
    input_str = input_str.strip()
    
    # Check for invalid comma placement
    if ',' in input_str:
        parts = input_str.split(',')
        if len(parts) != 2 or len(parts[1]) != 3:
            return "ERROR"
        input_str = input_str.replace(',', '')
    
    try:
        # Try to convert to float
        num = float(input_str)
        
        # Check if it's a whole number
        if num.is_integer():
            # If whole number, convert to int and then back to string
            return str(int(num))
        else:
            # If decimal, check if it has more than 2 decimal places
            if len(input_str.split('.')[-1]) > 2:
                return "ERROR"
            # Format to 2 decimal places
            return f"{num:.2f}"
    except ValueError:
        # If conversion fails, return ERROR
        return "ERROR"

# Main program
while True:
    user_input = input("Enter a number (or press Enter to exit): ")
    if user_input == "":
        break
    result = format_number(user_input)
    print(f"Input: {user_input}")
    print(f"Output: {result}")
    print()