#task 1

whole_sentence = "Python is amazing!"
python = whole_sentence[0:6]
print("First word: " + str(python))
amazing = whole_sentence[10:17]
print("Amazing part: " + str(amazing))
reversed = whole_sentence[::-1]
print("Reversed string: " + str(reversed))
print("\n")

#task 2

hello_world = " hello, python world! "
stripped = hello_world.strip()
print(stripped)
capitalized = stripped.capitalize()
print(capitalized)
replaced = capitalized.replace("world", "universe")
print(replaced)
uppered = replaced.upper()
print(uppered)


# task 3
print("\n")
user_input = str(input("Input a word: "))
user_reversed = user_input[::-1]
if (user_reversed == user_input):
    print("Yes, " + user_input + " is a palindrome!")
else:
    print("No, " + user_input + " is not a palindrome.")