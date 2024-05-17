# pi has been imported because it will need to be used later on
from math import pi

# The user will be asked if their foundation will be square, rectangular or round.
# The .lower() function has been used to make sure that if the user types SqUaRe etc it will still always be read as square
shape = input("What is your building shape? square, rectangular, round: ")
if shape.lower() == "square":
    square = True
else:
    square = False

if shape.lower() == "rectangular":
    rectangular = True
else:
    rectangular = False

if shape.lower() == "round":
    round == True
else:
    round == False

'''
I have commented this part of the code out. It wasn't a requirement but I wanted the program to recognise if the user didn't input any of the three key words. 
This part of the code works but all it does it displays you need to write either square, rectangular or round and then goes on to the next condition.
I wasn't sure how to loop it, but we haven't been taught about loops just yet.

if shape.lower() != "square" and shape.lower != "rectangular" and shape.lower != "round":
    print("You need to write either square, rectangular or round.")'''

# if the square was inputted then the user will be asked to input the dimensions of the square and then the area will be printed out.
if square == True:
    square_dimension = float(input("What is the length of the square in cm: "))
    square_area = square_dimension**2
    print(f"The area taken up by your square foundation building is {square_area} cm squared.")

# elif the user inputted rectangular then they will be prompted to input both the length and width of the rectangle. The area will then be printed out.
elif rectangular == True:
    rectangular_dimension_length = float(input("What is the length of the rectangle in cm? "))
    rectangular_dimension_width = float(input("What is the width of the rectangle in cm? "))
    triangle_area = rectangular_dimension_length * rectangular_dimension_width
    print(f"The area taken up by your rectangle foundation is {triangle_area} cm squared")

# else the user inputted round and they will be asked to type in the circle's radius. 
# pi was imported earlier so we can calculate the area of the circle (pi * radius **2)
# Python will then print the area of the circle.
else:
    radius = float(input("What is the radius of your circle in cm? "))
    circle_area = (pi * radius**2)
    print(f"The area taken up by your circle foundation is {circle_area} cm squared.")


    