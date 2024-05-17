menu = ["coffee", "carrot cake", "tea", "chocolate brownie"]

stock = {"coffee": 11,
         "carrot cake": 15,
         "tea": 35,
         "chocolate brownie": 9
         }

price = {"coffee": 3.25,
         "carrot cake": 3.10,
         "tea": 2.10,
         "chocolate brownie": 2.50
         }
# loop multiplies stock value * price value and prints individual price
result = {value: stock[value] * price[value] for value in stock}

print("The total cost for each item is:")
print(result["coffee"])
print(result["carrot cake"])
print(result["tea"])
print(result["chocolate brownie"])

# sum is used in front of multiplying stock value by price value to get the overall price
print("\nThe total amount of all items is:")
print(sum(stock[value]*price[value] for value in stock))



