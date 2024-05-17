#--------Task 1 -------#
# i is assigned the value 21 - remember that this means it will sdisplay 20 as its first number
i = 21

# while i is less than 21 - will keep subtracting 1 during each loop until i == 0 then the if statment and break will activate
print("Example 1:    ")
while i <= 21:
   i = i - 1
   print(i)
   if i == 0:
    break

# -------- Task 2 -------- #
# This for loop will check every number up to 20 and will only print the even numbers
# The even numbers are found by doing if i % 2 == 0
print("\nExample 2:    ")
for i in range(21):
    if i % 2 == 0:
        print(i)

# -------- Task 3 -------- #
# the first * is defined before the loop
# the for loop will add a * for every loop and stop at range 4 in the loop
print("\nExample 3:    ")

star = "*"
print("*")
for i in range(0,4):
    star = star + "*"
    print(star)

print("\nExample 4:    ")
# I wasn't sure if we needed to find the HCF using a loop? Luckily, we can just import math and do ,math.gcd(num1, num2) to find the HCF or GCD in python.
import math
num1 = int(input("What is your first number:  "))
num2 = int(input("What is your second number:   "))
print(f"The highest common factor of {num1} and {num2} is ",math.gcd(num1, num2))