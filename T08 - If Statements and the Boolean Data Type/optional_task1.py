# User is asked to input a number.
# The data is cast to an integer.
num = int(input("Enter a number : "))

# This if statement calculates if the number modulus of 2 is the same as 0 then it knows the number is even.
# If the number is not even then the else statement will print.
if num %2 == 0:
    print(f"Your number {num} is an even number.")

else:
    print(f"Your number {num} is an odd number.")
