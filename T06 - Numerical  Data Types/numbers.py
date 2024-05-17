import math
# The user will be asked to input three whole numbers of their choice.
first_num = input("Write a whole number: ")
second_num = input("What is your second whole number? ")
third_num = input("Now what is your final whole number? \n")

# This will cast each number from a string into an integer so Python can do the math.
first_num_int = int(first_num)
second_num_int = int(second_num)
third_num_int = int(third_num)

# The below statement uses addition to add the total of the three user numbers together.
num_total = first_num_int + second_num_int + third_num_int

# This will print the total of the three user numbers and display the output as an integer.
print(f"The total sum of your three numbers is: {num_total}\n")

# This variable will make the first number subtract the second number
first_num_minus_second_num = first_num_int - second_num_int
print(f"Your first number minus your second number gives you the answer: {first_num_minus_second_num}\n")

# The below code will multiply the 3rd number by the 1st number.
# When this gets printed out, the use of f string will show the actual number sentence using the numbers the user has chosen.
third_num_multiplied_by_first_num = third_num_int * first_num_int
print(f"{third_num_int} multiplied by {first_num_int} equals {third_num_multiplied_by_first_num}\n")

# This is a long variable name but I wanted to make sure that the variable would be understood by anyone reading. Is there a better way to write the variable whilst also keeping clarity of what it means?
sum_of_all_three_nums_divided_by_third_num = num_total / third_num_int
print(f"{first_num_int} + {second_num_int} + {third_num_int} / {third_num_int} = {sum_of_all_three_nums_divided_by_third_num}\n")

# It wasn't in the task, but I decided to have a go at importing math and flooring num_total / third_num_int to get the answer either rounded up or down to a whole number.
sum_floor = math.floor(sum_of_all_three_nums_divided_by_third_num)
print(sum_floor)
