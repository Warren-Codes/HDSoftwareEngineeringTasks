# ----- This program defines 3 functions - min, max, avg - which all take a list of numbers, calculates the min, max and
# avg number and returns their values. -------- #

# The minimum function uses the sorted_digits variable that has sorted all the numbers in the list from smallest to largest
# It returns the [0] index as this is the smallest index the sorted numbers will be
def minimum(sorted_digits):
    return sorted_digits[0]


# The maximum function uses the digit variable that has sorted all the numbers in the list from smallest to largest
# It returns the [-1] index as this is the largest index the sorted numbers will be
def maximum(digit):
    return digit[-1]


# The average function uses the digits variable and returns the sum of all the digits and divides this by the length of
# the digits
def average(digits):
    return sum(digits) / len(digits)

# The input.txt file opens for reading using the utf-8 encoder
# variables are manipulated with the .strip().split() functions to create a list where index 0 is either 'min', 'max' or
# 'avg' depending on the line and then index 1 has all the numbers. These numbers have been split at the comma and cast
# from a str to an int and then sorted from smallest to largest
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        components = line.strip().split(":")
        command = components[0]
        numbers = components[1].split(",")
        digits = [int(digit) for digit in list(numbers)]
        sorted_digits = sorted(digits)
        digit = sorted_digits

        # The output.txt file is opened with 'a' and if/elif statements run depending whether command.lower() == 'min',
        # 'max or 'avg'. The appropriate function is called and then the information gets written to the output file.
        lines = open('output.txt', 'a')

        if command.lower() == 'min':
            lines.writelines(f"The min of {digits} is {minimum(sorted_digits)}\n")

        elif command.lower() == "max":
            lines.writelines(f"The max of {digits} is {maximum(sorted_digits)}\n")

        elif command.lower() == "avg":
            lines.writelines(f"The avg of {digits} is {average(sorted_digits)}\n")

lines.close()
