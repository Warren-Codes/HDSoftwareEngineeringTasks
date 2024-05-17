# This variable is classed as an empty list by using []
incorrect_names = []

# While loop will keep asking the user to enter their name until they write "John"
# If the user types John then the loop breaks and each user_name is appended to the incorrect_names list
while True:
    user_name = input("Enter your name: ")

    if user_name.lower() == "john":
        break
    incorrect_names.append(user_name)

# This will print the amount of incorrect names, the names of the incorrect names in a list list and then the correct username.
print(f"You entered {len(incorrect_names)} incorrect names.\n"
      f"Incorrect User Names: {incorrect_names}\n"
      f"Correct User Name: {user_name}")
