
def calculator():
    first_input=int(input("Welcome to the Error-Free Calculator! Choose an operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Exit > "))
    if first_input < 5:
        try:
            first_number = int(input(" Enter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number next time.")
            return calculator()
        try:    
            second_number = int(input(" Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number next time.")
            return calculator()
        if (first_input == 1):
            sum1 = first_number + second_number
            print("The sum of " + str(first_number) + " and " + str(second_number) + " = " + str(sum1) + ".")
        elif (first_input == 2):
            difference = first_number - second_number
            print("The difference of " + str(first_number) + " and " + str(second_number) + " = " + str(difference) + ".")
        elif (first_input == 3):
            product = first_number * second_number
            print("The product of " + str(first_number) + " and " + str(second_number) + " = " + str(product) + ".")
        else:
            try:
                quotient = first_number / second_number
            except ZeroDivisionError:
                print("Oops! Division by zero is not allowed.")
                return calculator()
            else:
                print("The quotient of " + str(first_number) + " and " + str(second_number) + " = " + str(quotient) + ".")
    else: 
        print(" Exiting... ")

calculator()