# with open ("text_name.txt", "w") as f: will open the file for writing and close it automatically when it is finished
# an empty id_list [] is created which will have items appended to it later
with open("reg_form.txt", "w") as f:
    id_list = []

    # The user is asked to input how many students they wish to register
    registering = int(
        input("Enter the amount of students you are registering: "))

    # This for loop will run for the length of the interger inputted in the previous question
    # the registering variable has had range() added to it or you will get an error message int is not iterable
    for students in range(registering):
        id_num = int(input("Enter your ID number: "))

        # This will append each id_num to the empty id_list that was created at the start of the program. Each time the loop runs an extra
        # item will be appended to the list
        id_list.append(id_num)

    # Another for loop is created which will write the id_num for every id_num in id_list
    f.write("Student ID:\n")
    for id_num in id_list:
        f.write(f"{id_num}\n")

    # A dotted line will be written for a signature
    f.write("\nPlease sign on the dotted line\n\n"
            ".................................")
