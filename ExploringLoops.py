number = int(input("Enter an number: "))

while number != 0:
    print(str(number) + " ",end= '' )
    number -= 1

print("Blast off!")

number2 = int(input("Enter a second number: "))
current_product = 0
for i in range(1,11):
    current_product = number2 * i
    print(str(number2) + " x " + str(i) + " = " + str(current_product) + "  ", end='')
    current_product = 0

print("")

number3 = int(input("Enter a third number: "))
factorial = 1
for i in range(1,number3+1):
    factorial = factorial*i

print("The factorial of " + str(number3) + " is " + str(factorial))

