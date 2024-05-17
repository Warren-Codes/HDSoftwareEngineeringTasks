# This program allows a stock manager to undertake stock taking of shoes. The user can view all items, restock items,
# search for items and view specific items.

# Imported module
from tabulate import tabulate


# -------Defining the shoe Class------#

# Defines shoes class with the following parameters: country, code, product, cost, quantity
# Methods are defined which allows the user to perform a search

class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def get_country(self):
        return self.country

    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def set_quantity(self, quantity_new):
        self.quantity = quantity_new

    def __str__(self):
        return f"{OKGREEN}{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n".upper()


# -----Defining Functions -----#

# Opens the file for either reading or writing
# OKGREEN colour for text
# Empty lists for later

inventory_read = open("inventory.txt", "r")
inventory_write = open("inventory.txt", "a+")
OKGREEN = '\033[92m'

items_list = []
shoe_obj = []


# Try/finally is used in the event that the file does not exist for the user
# Read_shoes_data converts the data in the txt file ready for reading
# Each item is appended into an empty list
# Each item is converted into an object and appended to a new object list

def read_shoes_data():
    file = None
    try:
        for lines in inventory_read:
            data = lines.strip("\n").split(",")
            items_list.append(data)

        for i in range(1, len(items_list)):
            array = items_list[i]
            shoe1 = Shoes(array[0], array[1], array[2], array[3], int(array[4]))
            shoe_obj.append(shoe1)

    except FileNotFoundError:
        print(f"\n{OKGREEN}The file does not exist!\n")

    finally:
        if file is not None:
            file.close()


# Try/finally is used in the event that the file does not exist for the user
# Capture_shoes() function is defined that gets input for new products
# Each item is converted into an object and appended to object list
# The new information is written to the file and then closed

def capture_shoes():
    file = None

    try:
        new_country = input(f"{OKGREEN}Enter the country of your product:\n")
        new_code = input(f"{OKGREEN}Enter the product code:\n")
        new_product = input(f"{OKGREEN}Enter the product name:\n")
        new_cost = int(input(f"{OKGREEN}Enter the product cost in numbers\n"))
        new_quantity = int(input(f"{OKGREEN}Enter the product quantity in numbers\n"))

        new_shoe = Shoes(new_country, new_code, new_product, new_cost, new_quantity)
        shoe_obj.append(new_shoe)

        inventory_write.write(f'\n{new_country},{new_code},{new_product},{new_cost},{new_quantity}')
        print(f"{OKGREEN}\nYour product has been loaded!\n")

        inventory_write.close()

    except FileNotFoundError:
        print(f"{OKGREEN}\nSorry, this file does not exist!\n")

    finally:
        if file is not None:
            file.close()


# Try/finally is used in the event that the file does not exist for the user
# View_all() function displays all the shoes in the program
# Information for each product is got and displayed using tabulate module

def view_all():
    file = None

    try:

        print(f"{OKGREEN}\n" + "-" * 33 + "STOCK" + "-" * 33 + "\n")

        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        table = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_obj]

        print(tabulate(table, headers, tablefmt="pretty"))

        print(f"{OKGREEN}\n" + "-" * 33 + "END" + "-" * 33 + "\n")

    except FileNotFoundError as error:
        print(f"{OKGREEN}\nThe file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()


# Try/finally is used in the event that the file does not exist for the user
# Restock() function uses sort() to display the first 5 items that have the lowest stock
# Get info for each product using get_() class methods and this is displayed using tabulate module
# The user is asked to input the new stock quantity
# The information is written to the file and then the file gets closed

def restock():
    file = None

    restock_list = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []

    try:
        shoe_obj.sort(key=lambda x: x.quantity)

        for i in range(1, 6):
            restock_list.append(shoe_obj[i])

        print(f"{OKGREEN}\n" + "-" * 25 + "Lowest stock items:" + "-" * 25 + "\n")

        for line in restock_list:
            country.append(line.get_country())
            code.append(line.get_code())
            product.append(line.get_product())
            cost.append(line.get_cost())
            quantity.append(line.get_quantity())

        table = zip(country, code, product, cost, quantity)

        print(tabulate(table, headers=('Country', 'Code', 'Product', 'Cost', 'Quantity'), tablefmt='pretty',
                       showindex=range(1, 6)))

        print(f"{OKGREEN}\n" + "-" * 33 + "END" + "-" * 33 + "\n")

        user_input_item = int(input(f"{OKGREEN}\nEnter the index of the product you want to restock:\n"))
        user_input_qty = int(input(f"{OKGREEN}\nEnter the new quantity:\n"))
        shoe_obj[user_input_item].set_quantity(user_input_qty)

        output = ''
        for item in shoe_obj:
            output += (
                f'{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}\n')

        inventory_write_test = open("inventory.txt", "w")
        inventory_write_test.write(output)
        inventory_write_test.close()

        print(f"{OKGREEN}\nYour product has been updated!")

    except FileNotFoundError as error:
        print(f"{OKGREEN}\nThe file does not exist!\n")
        print(error)

    finally:
        if file is not None:
            file.close()


# Search_shoe() function displays a specific shoe
# Information for product using get_() class methods is displayed in the console

def search_shoe():
    search_shoe = input(f"{OKGREEN}\nEnter the code you are searching for:\n\n")

    for line in shoe_obj:
        if line.get_code() == search_shoe:
            print(f'\n {line}')

    print(f"{OKGREEN}\nSelect another option from the menu below\n")


# Value_per_item() function displays the value for a specific shoe
# Information for product using get_() class methods is displayed in the console

def value_per_item():
    for line in shoe_obj:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f'{OKGREEN}{line.get_code()} VALUE: £{value}\n')


# Highest_quantity() function displays the shoe with the highest quantity
# Empty list for quantity  value
# The quantity values are append to the empty list
# The max function is used to display the highest quantity
# The item gets put on sale

def highest_quantity():
    highest_qty = []

    for line in shoe_obj:
        highest_qty.append(line)

    print(f"{OKGREEN}\n----------------------------Highest stock item:----------------------------\n")

    print(max(shoe_obj, key=lambda item: item.quantity))
    print(f"{OKGREEN}\nThis item has now been marked on sale\n")
    print(f"{OKGREEN}\nPlease select an option from the menu below")


# -------- Main Program -------- #

# The menu options are displayed for the user
# Try/finally is used in the event that the file does not exist for the user
# Set ValueError
read_shoes_data()
while True:

    try:
        menu = int(input(f'''{OKGREEN}\n
            Select from the menu below:
            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            7. Exit
            \n\t\t\t'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            view_all()
            restock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_quantity()

        elif menu == 6:
            print(f"{OKGREEN}\nInvalid option. Try again by choosing from the menu below.\n")

        elif menu == 7:
            print(f"{OKGREEN}Goodbye.")
            break

    except ValueError:
        print(f"{OKGREEN}\nInvalid option. Enter a valid number.")

# ----- End of program ----- #