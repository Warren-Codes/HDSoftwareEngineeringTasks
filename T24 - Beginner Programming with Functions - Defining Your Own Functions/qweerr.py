# ----- This program defines 3 functions - min, max, avg - which all take a list of numbers, calculates the min, max and
# avg number and returns their values. -------- #
def minimum(sorted_digits):
    return sorted_digits[0]


def maximum(digit):
    return digit[-1]


def average(digits):
    return sum(digits) / len(digits)


    if x == 'min':
        result = min_value(nums)[0]
    elif x == 'max':
        result = max_value(nums)[-1]
    elif x == 'avg':
        result = avg_value(nums)

with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        components = line.strip().split(":")
        command = components[0]
        numbers = components[1].split(",")
        digits = [int(digit) for digit in list(numbers)]
        sorted_digits = sorted(digits)
        digit = sorted_digits
        lines = open('output.txt', 'w')
        if command.lower() == 'min':
            lines.writelines(f"The min of {digits} is {minimum(sorted_digits)}\n")

        elif command.lower() == "max":
            lines.writelines(f"The max of {digits} is {maximum(sorted_digits)}\n")

        elif command.lower() == "avg":
            lines.writelines(f"The avg of {digits} is {average(sorted_digits)}\n")
        lines.close()
        #sorted_digits_list = []
        #sorted_digits_list.append(sorted_digits)


        # temp = sorted_digits_list
        # print(sorted_digits_list)

# lines = open('output.txt', 'w')
# for line in lines:
#     f.write(f"The min of {digits} is {minimum(sorted_digits)}\n")
#     f.write(f"The max of {digits} is {maximum(sorted_digits)}\n")
#     f.write(f"The avg of {digits} is {average(sorted_digits)}\n")
# lines.close()


