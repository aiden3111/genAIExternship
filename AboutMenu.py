given = int(input("Welcome to the Recursive Artistry Program! Choose an option: 1. Calculate Factorial 2. Find Fibonacci 3. Fraw a Recursive Fractal 4. Exit > "))
def factorial(n):
    if (n==1 or n==0):
        return 1
    else: 
        return (n*factorial(n-1))
    
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n - 1) + fibonacci(n-2)

if (given == 1):
    factorial_number = int(input("Enter a number to fine its factorial: "))
    print(" The factorial of " + str(factorial_number) + " is " + str(factorial(factorial_number)) + ".")
elif (given == 2):
    fibonacci_number = int(input("Enter the position of the Fiboacci number: "))
    print("Number " + str(fibonacci_number) + " in the Fibonacci sequence is " + str(fibonacci(fibonacci_number)))
elif (given == 3):
    print("Turtle function not yet implemented.")
elif (given == 4):
    print("Exiting...")
else:
    print("Input not accepted, please try a number in the list.")