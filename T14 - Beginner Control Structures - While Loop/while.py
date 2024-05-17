# user is asked to input a number
user_input = int(input("Enter a number: "))

total = user_input
sum = 0

# this while loop is True providing the user's input does not equal -1
while user_input != -1:
    sum += user_input   # short hand for sum = sum + user_input
    user_input -= 1   # short hand for user_input = user_input - 1

    user_input = int(input("Enter a number: "))   # this is copied from the initial input and pasted into the while loop to make it continuous until the if statement is activated

if user_input == -1:        # this gets activated if the user inputs -1
    total_num_used = sum/total      # the total amount of numbers used is sum / total user inputs
    average = sum/total_num_used    # the average is calculated by the total sum divided total_num_used
    print(f"{sum} / {total_num_used} gives you an average {average}")