# The user will be prompted to input their full name.
full_name = (input("Please enter your full name : "))

# The character length of the user's full name is then turned into an integer.
full_name_int = int(len(full_name))

# If the user does not input anything they will be told they haven't entered anything.
if full_name_int == 0:
    print("You haven't entered anything. Please enter your full name.")

# Elseif the character length is greater than 0 and less than or equal to 4 then they will be prompted that their name has less than 4 characters.
elif full_name_int > 0 and  full_name_int <= 4 :
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname") 

# Elsif the user's name has a length of or greater than 25 they will be prompted that they have entered more than 25 characters.
elif full_name_int >= 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# If none of the other conditions are met, then the program will know that the user has entered their full name and it will thank them.
else:
    print("Thank you for entering your name")

