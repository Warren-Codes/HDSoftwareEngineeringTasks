num = int(input("Please enter a number: "))
if num %2 == 0 and num %5 == 0:
    print(f"The number {num} is divisble by 2 and 5.")
elif num %2 == 0 or num %5 == 0:
    print(f"The number {num} is divisible by 2 or 5.")
else:
    print(f"The number {num} is not divisible by 2 or 5.")