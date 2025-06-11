# task 1

given_number = str(input("Enter a number: "))
try:
    quotient = (100/int(given_number))
except ZeroDivisionError:
    print(" Oops! You cannot divide by zero. ", end = '')
except ValueError:
    print(" Invalid input! Please enter a valid number.", end = '')
else:
    print("100 divided by " + str(given_number) + " is " + str(quotient))


# task 2

students = ["garry", "larry"]
try:
    third = students[2]
except IndexError:
    print("IndexError occured! List index out of range. ", end = '')

grades = {"math": "A", "english": "B"}
try:
    new = grades["science"]
except KeyError:
    print("KeyError occured! Key not found in the dictionary. ", end = '')

try:
    new_sum = "Hello" + 1
except TypeError:
    print("TypeError occured! Unsupported operand types.")


# task 3

number1 = int(input("Enter the first number: "))
number2 = int(input(" Enter the second number: "))
try: 
    new_quotient = number1 / number2
except ZeroDivisionError:
    print(" Oops! You cannot divide by zero. ", end = '')
except ValueError:
    print(" Invalid input! Please enter a valid number.", end = '')
else: 
    print("The result is " + str(new_quotient), end = '')
finally:
    print(" This block always executes.")