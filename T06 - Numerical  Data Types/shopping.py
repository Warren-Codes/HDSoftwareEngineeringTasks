# The user will be presented with a greeting asking them to input any 3 items they wish to buy.
print("\t Imagine you can have any three items that you want. What would they be?\n")
item_1 = input("First item: ")
item_2 = input("Second item: ")
item_3 = input("Third item: ")

# The user will then be asked to write the value of each item to two decimal places.
print("\t Thank you. Now please tell us the price in £ and p of each of your chosen items. Your prices need to be to 2 decimal places, so if the price is £5 please write this as £5.00\n")
price_item_1 = input(f"Price of {item_1}: ")
price_item_2 = input(f"Price of {item_2}: ")
price_item_3 = input(f"Price of {item_3}: \n")

# This will cast each value to a float so Python to can math
float_price_item_1 = float(price_item_1)
float_price_item_2 = float(price_item_2)
float_price_item_3 = float(price_item_3)

# This will add up the total of the 3 items and print the calculated total.
item_total = float_price_item_1 + float_price_item_2 + float_price_item_3
print(f"The grand total of your three items is: £{item_total}\n")

# To make it easier to find the average, the total gets rounded to a whole number.
# To work out the average you must divide your item_total by the amount of items altogether. In this case, there are 3 items altogether so we rounded_item_total /3
rounded_item_total = round(item_total)
average_item_price = rounded_item_total / 3
print(f"The average price for each item is: £{average_item_price}\n")

# The below statement will tell the user the names, grand total and average price for each item.
print(f"The total of your items - {item_1}, {item_2} and {item_3} - is £{item_total}, and the average price of each item is £{average_item_price}")