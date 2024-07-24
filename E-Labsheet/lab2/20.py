age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))
nottax = income 
tax = 0
if age > 14 and age < 60 :
    if income > 0 and income < 80000 :
        if income > 0 and income <= 30000 :
            tax = income * 0.2
            print(f"Your negative income tax is {tax:.2f} Baht.")
        elif income > 30000 :
            tax = (80000-income)*0.12 
            print(f"Your negative income tax is {tax:.2f} Baht.")
    elif income >= 80000 :
        print("Invalid income.")
else :
    print("Invalid age.")
