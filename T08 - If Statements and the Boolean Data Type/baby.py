# This variable will ask the user what year they were born. The string has been converted to an integer with the use of int at the beginning.
# The age variable subtracts the user's input age to the current year to reveal their age.

birth_year = int(input("What year were you born? For example, if you were born in 1995 then write 1995 not 95 : "))
age = 2022 - birth_year

# This if statement will check to see if the user is 18 years old or over. If this condition has been met then the program will print "Congrats, you are old enough."

if age >= 18:
    print("Congrats, you are old enough.")


