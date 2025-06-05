name = "Aiden"
age = 21
height = 5.9

print("Hey there, my name is " + name + " I'm " + str(age) + " years old and " + str(height) + " feet tall")

num1 = 2
num2 = 5


print("The sum of 2 and 5 is", num1 + num2)
print("The product of 2 and 5 is", num1 * num2)
print("The quotient of 2 and 5 is", num1 / num2)
print("The difference of 2 and 5 is", num1 - num2)

num3 = int(input("Enter a number: "))

if (num3> 0):
    print("This number is positive. Awesome!")
elif (num3 < 0):
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")