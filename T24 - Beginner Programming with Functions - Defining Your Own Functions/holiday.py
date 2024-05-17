# This program defines 4 functions that are needed for a holiday calculator.

# ------- Function One ---------#
# This first function uses the number of nights the user would like to stay in a hotel and returns the total cost of
# staying in the hotel
def hotel_cost(nights):
    cost = 145.99
    total_cost = nights * cost
    return total_cost


# ------- Function Two ----- #
# This second function uses the city the user would like to travel to as an argument and returns the plane cost
# depending on the destination, with different values being returned via if/else statements.

def plane_cost(city):
    if city == "Paris":
        return 275

    elif city == "Amsterdam":
        return 230

    elif city == "Berlin":
        return 170

    elif city == "Miami":
        return 745

    elif city == "Sydney":
        return 1240

    elif city == "Auckland":
        return 1430

    elif city == "None":
        return 0

    else:
        print("You did not make a valid selection.")


# -------- Function Three -------#
# This third function takes in the amount of days a user would like to hire a car for as an argument and returns the
# total car rental cost.

def car_rental(days):
    total_car_cost = 80 * days
    return total_car_cost


# -------- Function Four ------ #
# This fourth function uses the nights to stay in a hotel, the city destination and number of days to hire a car for
# as arguments and returns the total cost of the holiday as well as prints out confirmation of each choice made by
# the user
def holiday_cost(nights, city, days):
    print(f"You would like to stay in the hotel for {nights} nights.\n")
    print(f"The destination for your holiday you have chosen is {city}.\n")
    print(f"You have chosen to hire the car for {days} days.\n")
    return hotel_cost(nights) + plane_cost(city) + car_rental(days)

# variables where the user inputs their choices
nights = int(input("How many nights will you be staying at the hotel for: "))

city = input("Please type a destination below you would like to visit:\n"
             "Paris\n"
             "Amsterdam\n"
             "Berlin\n"
             "Miami\n"
             "Sydney\n"
             "Auckland\n"
             "None\n\nI would like to vist: ").capitalize()

days = int(input("How many days would you like to rent a car for? "))

# The holiday_cost function is called which calls the three other functions, returns all the values and prints the
# total cost of the holiday
print(f"The total cost of your holiday is £" + str(holiday_cost(nights, city, days)))
