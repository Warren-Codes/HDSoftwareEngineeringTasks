friend_names = ["Ian", "John", "Bob"]
print(friend_names[0])      # prints Ian
print(friend_names[2])      # Prints Bob
print(len(friend_names))    # Prints the length of the list

friend_ages = [34, 35, 33]
print(friend_ages)

# The below uses a for loop so all names are printed. friend_ages has been indexed so each statement will print the friends name and age.
for name in friend_names:

    if name == "Ian":
        print(f"{name} is {friend_ages[0]}")
    if name == "John":
        print(f"{name} is {friend_ages[1]}")
    if name == "Bob":
        print(f"{name} is {friend_ages[2]}")
