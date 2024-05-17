# This program asks a user for 10 numbers as floats and then prints the sum, max, min, average rounded to 2 d.p.
# and median numbers all taken from the user input.

# imports the math and statistics module
import math
import statistics

# Empty float_list that will have information appended to later
float_list = []

# for loop iterates 10 times by using range(10)
# user will be asked to input a number 10 times
# each number will be appended to float_list
for numbers in range(10):
    user_input = float(input("Enter a number with at least 1 decimal point: "))
    float_list.append(user_input)

# str((sum(float_list))) to print the total of all the numbers user enters.
# float must be converted to a string to enable concatenation
print("\nThe total of your 10 numbers adds up to " + str((sum(float_list))) + ".")

# max(float_list) and min(float_list) assigns the min and max of the 10 numbers to the variables 'maximum' and 'minimum'
maximum = max(float_list)
minimum = min(float_list)
print(f"The minimum number is {minimum} and the maximum number is {maximum}.")

# statistics.mean(float_list) will find the average of the float_list
# the average has been assigned to the 'average' variable
average = statistics.mean(float_list)

# average is rounded to two decimal places by calling the round(average, 2) function and casting it to a str to
# concatenate it.
print("The average of your numbers rounded to two decimal places is " + str((round(average, 2))) + ".")

# statistics.median(float_list) uses the statistics module to find the median of the numbers in float_list
print("The median of your numbers is " + str(statistics.median(float_list)) + ".")


