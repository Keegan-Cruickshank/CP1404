"""
Keegan Cruickshank
"""

min_length_of_password = 8
password_input = input("Enter a password: >")
while not len(password_input) >= 8:
    print("Password needs to be {} or more characters long".format(min_length_of_password))
    password_input = input("Enter a password: >")
for char in password_input:
    print("*", end="")