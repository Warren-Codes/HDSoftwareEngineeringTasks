# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program\n")


age = 27
print(f"I'm {age}years old.")





answer_months = (age * 12) + 6
print(f"In 3 years and 6 months, I'll be {answer_months} months old.")

#HINT, 330 months is the correct answer



# Line 6 is a syntax error as it does not have brackets for the print command.
# Line 7 is a syntax error as it is indented when it shouldn't be. It's also better to just use \n for a new line at the end of line 6.
# Line 9-12 are indented when they shouldn't be.
# Line 9 also uses double == when only one = is needed to assign a variable. You also cannot cast an integer to a 3 word string.
# Lines 9 -12 are trying to say that the user is 27 years old so it is easier to simply assign the age variable to 27 and delete the rest.
# Line 10 a f string is now used to include the age variable. There were too many inverted commas.
# Line 13 answerYears is not even needed.
# Line 15 is not needed, plus there is a runtime error as you cannot concatenate a string and integer.
# Line 16 the variable needs an _ and this will also produce a logical error as the user is forgetting to add an extra 6 months for so it is 3.5 years and not 3 years.
# Line 16 I have changed the variable 'answer' to 'age' otherwise there'd be a run time error.
# Line 17 is a syntax error as there are no brackets for the print command. An f string is needed to insert the variable into a string as you cannot concatenate strings with ints