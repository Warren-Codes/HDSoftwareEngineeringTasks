num1 = input("Tell me a number ")
num2 = input("Now tell me a second number ")
print (f"\nThe first number you picked was: {num1} \nThe second number you picked was: {num2}\n")

num1, num2 = num2, num1
print(f"Your first number has now been swapped to the second number: {num1} \nYour second number has now been swapped to your first number: {num2}")