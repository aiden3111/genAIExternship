age = int(input("How old are you? "))
if (age >= 18):
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    years_needed = 18 - age
    print("Oops! You're not eligibile yet. But hey, only " + str(years_needed) + " to go!") 