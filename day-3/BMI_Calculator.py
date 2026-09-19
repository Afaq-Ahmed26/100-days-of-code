weight = int(input("Enter your weight in kg: "))
height_in_feet = int(input("Enter your height in feet: "))
height_in_inch = int(input("Enter your height in inches: "))
height_in_inches = height_in_feet * 12 + height_in_inch

# Convert height from feet to meters
height_in_meters = height_in_inches * 0.0254

# Calculate BMI
bmi = weight / (height_in_meters ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("slightly overweight")
elif bmi >= 30 and bmi < 35:
    print("obese")
else:
    print("clinically obese")
