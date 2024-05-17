# There are 3 numbers num1, num2 and num3.
# To work out the smallest, middle and largest numbers there are small, middle and large vaiables we will assign later.
num1 = 10
num2 = 20
num3 = 30
small = 0
middle = 0
large = 0

# compare num1 and num2 and display the larger value
# < less than
# > greater than
if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)

# to check if a number is odd or even
# modulus 2 will check to see if a number is divisible by 2 with no remainders
# if no remainders then the number is even
# if a remainder then the number is odd
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")


# To determine the smallest number
# if num1 is smaller than num2 and smaller than num3 then num1 is the smallest number
# elif num2 is smaller than num1 and smaller than num3 then num2 is the smallest number
# else num3 is smallest
if num1 < num2 and num1 < num3:
    small = num1
elif num2 < num1 and num2 < num3:
    small = num2
else:
    small = num3

# To determine the middle number
# if num1 is greater than num2 and less than num3 then num1 is the middle number
# elif num2 is greater than num1 and less than num3 then num2 OR num2 is smaller than num1 and greater than num3 then num2 is the middle number
# else num3 is the middle
if num1 > num2 and num1 < num3:
    middle = num1
elif num2 > num1 and num2 < num3:
    middle = num2
elif num2 < num1 and num2 > num3:
    middle = num2
else:
    middle = num3

# To determine the large number
# if num1 is larger than num2 and num3 then num1 is the largest number
# elif num2 is larger than num1 and num3 then num2 is the largest number
# else num3 is the largest number
if num1 > num2 and num1 > num3:
    large = num1
elif num2 > num1 and num2 > num3:
    large = num2
else:
    large = num3

#The below will print the variables small, middle, large now the appropriate numbers have been assigned to them.
print(small, middle, large)

