special_characters = "@#$!?"
password = str(input("Enter a password: "))
password_length = len(password)
while True:
    if password_length < 8:
        print("Password length must be at least 8 digits/letters")
        break
    has_digit = False
    has_uppercase = False
    has_lower = False
    has_special = False
    for char in password:
        if char.isdigit() == True:
            has_digit= True
        if char.isupper() == True:
            has_uppercase = True
        if char.islower() == True:
            has_lower = True
        if char in special_characters:
            has_special = True
    error_message = "Your password must contain:"
    if has_uppercase == False:
        error_message = error_message + " at least one uppercase letter;"
    if has_lower == False:
        error_message = error_message + " at least one lowercase letter;"
    if has_digit == False:
        error_message = error_message + " at least one digit;"
    if has_special == False:
        error_message = error_message + " at least one special character"
    error_message = error_message + "."
    if (has_digit == True) and (has_lower == True) and (has_special == True) and (has_uppercase == True):
        print("Your Password is strong!")
        break
    else:
        print(error_message)
        break