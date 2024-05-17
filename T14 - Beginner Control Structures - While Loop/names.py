total_names = 0

names = (input("Please enter all of the names of the children in your class. Type 'Stop' when you have finished: "))
   
while names.lower() != "stop":
    total_names += 1  # The same as total_names = total_names + 1

    names = (input("Please enter all of the names of the children in your class. Type 'Stop' when you have finished: "))

    if names.lower() == "stop":     # .lower() will make sure the input will always come back lower case
        print(total_names)
        
        break 