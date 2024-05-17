while True:
    try:
        user_num_1 = int(input("Enter your first whole number. Type \"-1\" to exit: "))
        if user_num_1 == -1:
            break
        else:
            user_num_2 = int(input("Enter your second whole number: " ))
            operator = input("Enter your operator '*', '/', '+', or '-': ")
            result = eval(f"{user_num_1}  {operator}  {user_num_2}")
            print(result)
            with open("calculator.txt", "w+") as f:
                f.write(f"{user_num_1} {operator} {user_num_2} = {result}")


    except ValueError:
        print("Oh dear, you didn't enter a whole number.")


    except ZeroDivisionError:
        print("You cannot divide by 0")

    except SyntaxError:
        print("You didn't enter an operator: + to add, - to subtract, * to multiply, / to divide")




    #
    #

