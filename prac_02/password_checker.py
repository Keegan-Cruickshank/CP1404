"""

Sorry guys, i took the DO_FROM_SCTRATCH Github instruction to literal
and did it all without starter code without realising :)

"""
MIN_PASSWORD_LENGTH = 5
MAX_PASSWORD_LENGTH = 15
SPECIAL_CHARS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

print("Please enter a valid password")
print(
    "Your password must be between {} and {} characters, and contain:".format(
        MIN_PASSWORD_LENGTH,
        MAX_PASSWORD_LENGTH))
print("   1 or more uppercase characters")
print("   1 or more lowercase characters")
print("   1 or more numbers")
print("   and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\\")


valid_password = False

while not valid_password:
    user_password_attempt = input(">>>")
    if MIN_PASSWORD_LENGTH < len(user_password_attempt) < MAX_PASSWORD_LENGTH:
        """
        If the quantity of each characters in the password needed
        to be greater then one, I would just change below to counters and add one if they are found.
        For now, I find reading the Booleans easier.
        """
        has_uppercase = False
        has_lowercase = False
        has_number = False
        has_special = False
    else:
        print(
            "Password must be between {} and {} in length. Try Again.".format(
                MIN_PASSWORD_LENGTH,
                MAX_PASSWORD_LENGTH))
        user_password_attempt = input(">>>")

    for char in user_password_attempt:
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
        if char.isdigit():
            has_number = True
        for possible_special in SPECIAL_CHARS:
            if ord(possible_special) == ord(char):
                has_special = True

    if has_number and has_special and has_uppercase and has_lowercase:
        valid_password = True
    elif not has_lowercase:
        print("You need at least one lower case letter")
    elif not has_uppercase:
        print("You need at least one upper case letter")
    elif not has_number:
        print("You need at least one number")
    elif not has_special:
        print("You need at least one special character")
print("You did it, Awesome Password!")
