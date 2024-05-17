


def hotel_cost(nights):
    night = int(input("How many nights will you be staying at the hotel for: "))
    cost = 145.99
    total_cost = nights * cost
    print(f"You would like to stay in the hotel for {night} nights.\n")
    return total_cost


def plane_cost(city):
    while True:
        city_input = input("Please type a destination below you would like to visit:\n"
                     "Paris\n"
                     "Amsterdam\n"
                     "Berlin\n"
                     "Cape Town\n"
                     "Sydney\n"
                     "Auckland\n"
                     "None\n\nI would like to vist: ").capitalize()
        city = city_input
        print(f"The destination for your holiday you have chosen is {city}.\n")
        if city.capitalize() == "Paris":
            return 275

        elif city.capitalize() == "Amsterdam":
            return 230

        elif city.capitalize() == "Berlin":
            return 170

        elif city.capitalize() == "Cape Town":
            return 580

        elif city.capitalize() == "Sydney":
            return 1240

        elif city.capitalize() == "Auckland":
            return 1430

        elif city.capitalize() == "None":
            return 0

        else:
            print("You did not make a valid selection.")
        continue


def car_rental(days):
    rental = int(input("How many days would you like to rent a car for? "))
    total_car_cost = 55 * rental
    print(f"You have chosen to hire the car for {rental} days.\n")
    return total_car_cost


def holiday_cost(nights, city, days):
    return hotel_cost(nights) + plane_cost(city) + car_rental(days)


print(f"The total cost of your holiday is £" + str(holiday_cost(1, 1, 1)))


# hotel_cost()
# plane_cost()
# car_cost()
# holiday_cost()
