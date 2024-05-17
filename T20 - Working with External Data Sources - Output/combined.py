# ----------- FILE 1 ---------- #
# This will open/create a numbers1.txt file ready for writing, as denoted by 'w'
with open("numbers1.txt", "w") as f:

    # An empty num list to store our num for each loop
    num_list = []

    # The numbers 1-100 will be written
    for num in range(0, 101):

        # Each num will be appended to the num_list
        num_list.append(num)

    # Each num will be printed on a new line from 1-100
    for num in num_list:
        f.write(f"{num}\n")

# ----------- FILE 2 -------- #
# This will open/create a numbers.2txt file ready for writing, as denoted by 'w'
with open("numbers2.txt", "w") as f:

    # An empty num list to store our num for each loop
    num_list = []

    # The numbers 101-200 will be written
    for num in range(101, 201):

        # Each num will be appended to the num_list
        num_list.append(num)

    # Each num will be printed on a new line from 101-200
    for num in num_list:
        f.write(f"{num}\n")


# -------- FILE 3 ----------#
# -------- This will merge the two files into one file ---------- #

# A new list is created which includes the previous two txts - numbers1.txt. and numbers2.txt
files_to_merge = ['numbers1.txt', 'numbers2.txt']

# A new number list is created from the nums in the files_to_merge_list
# The information in the two txt files is opened using open(f) and they are read, stripped of all white space and then split
num_lists = [[int(num) for num in open(f).read().strip().split('\n')]
             for f in files_to_merge]

# This will open/create an all_numbers.txt file ready for writing, as denoted by 'w'
with open('all_numbers.txt', 'w') as f:

    # The num variable has been made into a str ready to be written.
    # the sorted command has been used to ensure that the numbers go from smallest to largest
    f.write('\n'.join(str(num) for num in sorted(sum(num_lists, []))) + '\n')
