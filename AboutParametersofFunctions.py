#task 1

def greet_user(name, number1, number2, sum):
    print("Hello, " + str(name) + "! Welcome aboard. The sum of " + str(number1) + " and " + str(number2) + " is " + str(sum) + ".")

def add_numbers(number1, number2):
    return (number1 + number2)

given_name = str(input("Enter a name: "))
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
sum_of_two = add_numbers(first_number, second_number)

greet_user(given_name, first_number, second_number, sum_of_two)


# task 2

def describe_pet(pet_name, animal_type="dog"):
    print("I have a " + str(animal_type) + " named " + str(pet_name) + ".", end='')

animal_name = str(input("Enter your pet's name: "))
species = str(input("Enter animal type: "))

describe_pet(animal_name, species)

# task 3

def make_sandwich(*args):
    print("\nMaking a sandwich with the following ingredients: ", end = '')
    for i in args:
        print(" - " + str(i) + " ", end = '')

make_sandwich("Lettuce", "Tomato", "Cheese")

# task 4

def factorial(number):
    fact = 1
    for i in range(1, number+1):
      fact = fact * i
    return fact

def fibonacci(n):
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b

print("\nFactorial of 5 is " + str(factorial(5)) + ". The 6th Fibonacci number is " + str(fibonacci(6)) + ".")