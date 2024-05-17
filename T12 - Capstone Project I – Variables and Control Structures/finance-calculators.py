import math


# The user is asked to input 'investment' or 'bond'
investment_or_bond = (input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment \t - \t"
                        "to calculate the amount of interest you'll earn on your investment\n"
                        "bond          \t - \tto calculate the amount you'll have to pay on a home loan\n"))

####### START OF INVESTMENT CALCULATOR ##########

# if the user types 'investment' then they will be asked how much money they would like to deposit, the interest rate of the savings, how many years they plan to save for
# and whether they want simple or compound interest
if investment_or_bond.lower() == 'investment':
    deposit = float(input("How much money would you like to deposit into your investment in £? If '£1000' simply imput 1000: "))
    interest_rate = float(input("What is the interest rate as a percentage? If '8%' simply input 8:  "))
    investment_years = int(input("For how many years do you plan on investing: "))
    interest = (input("What interest type would you like? Simple or compound? "))

    # This shows the variables used in the interest formula calculation.
    r = interest_rate / 100
    p = deposit
    t = investment_years

    ############# SIMPLE INTEREST ############

    # simple interest is calculated as the amount the user deposits * 1 + interest rate * investment years
    # in python this equates to p*(1+r*t)

    # This will clarify the options to the user and tell them how much interest they will make and what their overall investment will be after x years
    # the round function has been used to ensure that the answers are given to 2dp as we are using money
    # a has been assigned the simple interest formula
    # i will calculate the amount of interest alone that has been accrued

    if interest.lower() == "simple":
        a = p*(1+r*t)
        i = a - deposit
        print(f"\nYou would like to deposit £{deposit} with an interest rate of {interest_rate}% for {investment_years} years and you have chosen for your interest"
        f"to be {interest}.\n"
        f"You will make £{round(i, 2)} in interest over {investment_years} years which will bring your total balance to £{round(a, 2)} after {investment_years} years.")
    
    ######### COMPOUND INTEREST ########

    # Compound interest is calculated as the amount the user deposits * math.pow((1 + interest rate), investment years)
    # The formula for compound interest is thus: a = p* math.pow((1+r),t)

     # This will clarify the options to the user and tell them how much interest they will make and what their overall investment will be after x years
    # the round function has been used to ensure that the answers are given to 2dp as we are using money
    # a has been assigned the simple interest formula
    # i will calculate the amount of interest alone that has been accrued

    elif interest.lower() == "compound":
        a = p* math.pow((1+r),t)
        i = a - deposit
        print(f"\nYou would like to deposit £{deposit} with an interest rate of {interest_rate}% for {investment_years} years and you have chosen for your interest to be {interest}.\n"
        f"You will make £{round(i, 2)} in interest over {investment_years} years which will bring your total balance to £{round(a, 2)} after {investment_years} years.")

####### END OF INVESTMENT CALCULATOR #######

######## START OF BOND CALCULATOR ########

# if the user inputs 'bond' then they will be asked a range of new questions asking them the current house value, the interest rate and for how long they want to have the bond
# The inputs have been converted to a float
elif investment_or_bond.lower() == "bond":
    house_value = float(input("What is the current value of the house in £ (eg 150000): "))
    bond_interest = float(input("What is the interest rate on the house bond (eg 7): "))
    bond_months = float(input("For how many months do you plan on repaying the bond (eg 120): "))

    # This shows the variables used in the bond interest calculator
    p = house_value
    i = bond_interest / 100*(1/12)    # This divides the interest rate by 100 and then multiplies by one twelfth to get the monthly value 
    n = bond_months
    monthly_repayment = (i * p)/(1 - (1+i)**(-n))   #monthly-repayment = (bond_interest * house_value) / (1-(1+bond_interest)**(-bond_months)) 
   
    # this will clarify the options to the user and tell them how much their monthly repayment will be over x months
    # the round function has been used to ensure that the answers are given to 2dp as we are using money
    print(f"\nYour current house value is £{house_value} and your bond interest rate is {bond_interest}% and you would like to repay over {bond_months} months.\n"
    f"You will need to repay £{round(monthly_repayment,2)} every month for {bond_months} months.")




        

