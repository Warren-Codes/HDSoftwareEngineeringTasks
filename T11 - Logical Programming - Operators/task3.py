# The user is asked to input their swimming, cycling and running times.
# The user's total time will be calculated by adding their swimming, cycling and running time together.
swimming_time = float(input("How many minutes did you take swimming? "))
cycling_time = float(input("How many minutes did you take cycling?" ))
running_time = float(input("How many minutes did you take running? "))
total_time = swimming_time + cycling_time + running_time

# If the user's total time is 100 or less minutes then they get a provincial colours award.
# If the user's time is between 101-105 minutes they get a provincial half colours award.
# if the user's time is between 106-110 minutes they get a provincial scroll award.
# if the user's time is greater than 110 minutes then they get no award.
if total_time <= 100:
    print(f"Congratulations! Your total time is {total_time} minutes which means you have recieved the Provincial Colours Award!")
elif total_time > 100 and total_time <= 105:
    print(f"You were slightly over the qualifying time. Your total time was {total_time} minutes which means you have recieved the Provincial Half Colours Award.")
elif total_time > 105 and total_time <= 110:
    print(f"You need to practice a bit more. Your total time was {total_time} minutes which means you have recieved the Provincial Scroll Award.")
else:
    print(f"Unfortunately your total time of {total_time} minutes was too slow and you have not recieved an award. Better luck next time!")
