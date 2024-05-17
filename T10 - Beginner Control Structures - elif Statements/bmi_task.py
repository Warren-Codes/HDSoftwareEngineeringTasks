# Variables that are used in the program.
# User input has been cast to float to do math
user_weight = float(input("How much do you weigh in kg? "))
user_height = float(input("How tall are you in m? "))
bmi = user_weight / user_height**2 

# if, elif, else conditions and statements are rounded to 2 decimal places.
if bmi >= 30:
    print(f"You are obese as your BMI is {round(bmi, 2)}.")
elif bmi >= 25:
    print(f"You are overweight as your BMI is {round(bmi, 2)}.")
elif bmi >= 18.5:
    print(f"Your BMI is in the normal range as it is {round(bmi, 2)}.")
else:
    print(f"You are underweight as your BMI is {round(bmi, 2)}.")
