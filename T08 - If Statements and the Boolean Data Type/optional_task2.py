weekend = True
degrees_20 = True
sunny = True

print("Good Morning!")

weekend_check = input("Is today the weekend? (Yes or No)")

if weekend_check == "No" or "no":
	weekend = False

degrees_20_check = input("Is it at least 20 degrees today?? (Yes or No)")

if degrees_20_check == "No" or "no":
	degrees_20 = False

sunny_check = input("Is it sunny outside? (Yes or No)")

if sunny_check == "No" or "no":
	sunny = False	

if weekend == True:
    trousers = "shorts"
else:
    trousers = "jeans"

if degrees_20 == True:
    shirt = "a short sleeve shirt"
else: 
    shirt = "a long sleeve shirt"

if sunny == True:
    hat_coat = "hat"
else:
    hat_coat = "coat"

print(f"Today you should wear {trousers}, {shirt} and a {hat_coat}.")