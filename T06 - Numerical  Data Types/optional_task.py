
import math

# The user is asked to write the lengths of a triangle. Length c specifies that it must be the longer diagonal as knowing this will help to calculate the area later.

print("\t\tImagine you have a triangle, please write, in mm, the length of each side")
length_a = input("The length of side a is: ")
length_b = input("The length of side b is: ")
length_c = input("The length of the long diagonal is: ")

# The above values need to be converted into an integer so Python can do the math.
int_length_a = int(length_a)
int_length_b = int(length_b)
int_length_c = int(length_c)

# To work out the area of a triangle you must multiply two sides together (this will give the area as if it were a rectangle) and then divide by 2 as the area of a triangle is half that of the rectangle.
# This is why it is important for the user to write the longest diagonal length last, in length c, because you do not use this length when calculating the area of a triangle.
triangle_area = int_length_a * int_length_b / 2
print(f"The area of your triangle is {triangle_area} mm squared.")






