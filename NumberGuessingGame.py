import random

number_to_guess = random.randint(1, 100)
number = -1
number = int(input("Guess the number (between 1 and 100): "))
count = 0

while number != number_to_guess:
    if (number > number_to_guess):
        print(number)
        number = int(input("Too High! Try again: "))
        count+=1
    elif (number < number_to_guess):
        print(number)
        number = int(input("Too Low! Try again: "))
        count+=1


count+=1
print(number)
print("Congratulations! You guessed it in " + str(count) + " attempts!")