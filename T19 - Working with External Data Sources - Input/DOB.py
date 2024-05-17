# The below command will open the DOB text and close it automatically when it is finished
# names_list and dob_list are assigned to an empty list
with open('DOB.txt', 'r+') as f:
    names_list = []
    dob_list = []

# A loop is created where each line is read by using the command f.readlines()
# A temporary variable line is created that strips the DOB file of all white space before and after a line
# Each word is split with an empty space " "
# The name variable is created by indexing the first and second item in the temp line list. The first and second items are the first and last names
#  The dob variable is created by indexing the 3,rd 4,th and fifth items in the temp line list. This creates the date of birth
    for line in f.readlines():
        temp = line.strip().split(" ")
        name = f"{temp[0]} {temp[1]}"
        dob = f"{temp[2]} {temp[3]} {temp[4]}"

        # For each iteration of the loop the name and dob variable will be appended to the names_list and dob_list, respectively
        names_list.append(name)
        dob_list.append(dob)

# In order to write to the DOB file you need to f.truncate and f.seek. f.seek is used because Names was missing at the start of the txt
    f.truncate(0)
    f.seek(0)

# This will write the names into the DOB.txt file
    f.write("Name\n")
    for name in names_list:
        f.write(f"{name}\n")

# This will write the DOB into the DOB.txt file
    f.write("\nBirthdate\n")
    for dob in dob_list:
        f.write(f"{dob}\n")
