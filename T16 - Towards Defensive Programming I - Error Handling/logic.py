
age = int(input("How old are you:   "))
if age >= 18 and age < 50:
    print("You may come in!")
    drink = (input("Would you like a whisky (y/n):"  ))
    if drink.lower() == "y":
        drink2 = (input("What would you like instead?    "))
           
        drink2 == "coke"
        if drink2 == "coke":
            print(f"Your {drink2} is coming right up!")
                
        else:
            print(f"Sorry, we do not have {drink2} in stock right now.\nPerhaps you should leave.")
           

    else:
         print("Great I will get you your whisky!")
elif age >= 50:
    print("You should go home and have a cup of tea and then go to bed.")
        
else:
    print("Go home you punk!")

# Can you spot my logical error? :D
        
    


