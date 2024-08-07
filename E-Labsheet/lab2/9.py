w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/(h**2)
print(f"BMI is {bmi:.1f}")
if bmi < 18.5 :
    print("Underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("Normal weight")
elif bmi >= 25 and bmi < 30 :
    print("Overweight")
else :
    print("Obesity")