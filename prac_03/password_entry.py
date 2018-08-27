"""
Keegan Cruickshank
"""


def main():
    password = get_password()
    print_hidden_password(password)


def print_hidden_password(password):
    for index in password:
        print("*", end="")


def get_password():
    min_length_of_password = 8
    password_input = input("Enter a password: >")
    while not len(password_input) >= 8:
        print("Password needs to be {} or more characters long".format(
            min_length_of_password))
        password_input = input("Enter a password: >")
    return password_input


main()
