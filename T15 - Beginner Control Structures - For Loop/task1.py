# the first for loop asks the user to input a times table they would like to see between 1 and 12
for x in range (1,13):
    x = int(input("What times tables would you like to see? Pick from 1 up to 12: "))
    if x <= 12:     # an if statement is used to determine if the number is between 1 and 12 that it then goes to the next forloop where it will display the answers
        print(f"The {x} times tables are:")
    else:           # the else statement will become active if the user enters a number greater than 12 and will display the text "You didn't choose between 1 and 12"
        print("You didn't pick a times table between 1 and 12.")
        continue    # the for loop will continue from the beginning if the else statement is activated

    # this is a nested for loop which will show {x} * {y} = {x * y}
    for y in range (1,13):
        print(f"{y} * {x} = {x * y}")
    print("")
   

