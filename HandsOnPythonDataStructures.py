# task 1
favorite_fruits = ["apple", "pear", "grape", "orange", "watermelon"]
print("Original list: " + str(favorite_fruits))
favorite_fruits.append("peach")
print("After adding a fruit: " + str(favorite_fruits))
favorite_fruits.remove("orange")
print("After removing a fruit: " + str(favorite_fruits))
print("Reversed list: " + str(favorite_fruits[::-1]))

# task 2

about_myself = {"name":"Aiden", "age":"21", "city": "NYC"}
print(about_myself)
about_myself["favorite color"] = "red"
print(about_myself)
about_myself["city"] = "DC"
print(about_myself)

print("Keys: ", end = ' ')
for key, value in about_myself.items():
    print(key, end = ' ')

print("\n")

print("Values: ", end=' ')
for value in about_myself:
    print(about_myself[value], end=' ')

print("\n")
# task 3

my_favorites = ("The Grand Budapest Hotel", "Tiny Dancer", "Berserk")
print("Favorite things: " + str(my_favorites))
print("Oops! Tuples cannot be changed.")

print("Length of tuple: " + str(len(my_favorites)))