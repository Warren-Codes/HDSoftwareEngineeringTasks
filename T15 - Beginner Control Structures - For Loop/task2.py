

# User is asked to input the start year and the increment value
year_start = int(input("What year do you want to start with:    "))
num_of_years = int(input("How many years do you want to check:  "))

# This variable is needed for the end value in the range so we know what year to stop at
added_years = year_start + num_of_years

# This for loop will check if the year is a leap year by seeing ifr it is a multiple of 4
# 'i is a leap year' will br printed if it is a leap year
# 'i is not a leap year' will be printed if it is not a leap year
for i in range(year_start, added_years):
    if (i %4 == 0 and i %100 != 0) or (i %400 == 0):
        print(i, "is a leap year.")
    else :
        print(i, "is not a leap year.")



