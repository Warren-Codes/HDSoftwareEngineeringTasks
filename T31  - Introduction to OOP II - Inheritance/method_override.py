# This program creates a class 'Adult' and a subclass 'Child'. Both classes initialise the attributes name, age,
# eye_colour and hair_colour. Within both of the classes is the method can_drive(): This method prints out that adults
# are old enough to drive whereas the method in the Child subclass overrides the Adult method as it prints out that
# child can not drive.

OKBLUE = '\033[94m'
UNDERLINE = '\033[4m'

class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"\n{OKBLUE}{UNDERLINE}{self.name} is {self.age} so is old enough to drive.")


class Child(Adult):
    def can_drive(self):
        print(f"\n{OKBLUE}{UNDERLINE}{self.name} is {self.age} so is not old enough to drive.")

# Input variables are created for the user to type in their own information
name = input(f"{OKBLUE}Enter your name: ")
age = int(input(f"{OKBLUE}Enter your age: "))
eye_colour = input(f"{OKBLUE}Enter your eye colour: ")
hair_colour = input(f"{OKBLUE}Enter your hair colour: ")

# If the user is >= 18 then they are assigned the Adult class.
# If the user is < 18 then they are assigned the child class.
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)

else:
   person = Child(name, age, eye_colour, hair_colour)

# can_drive method is called which prints whether the person can or can not drive.
person.can_drive()