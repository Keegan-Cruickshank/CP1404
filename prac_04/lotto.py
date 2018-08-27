""" Application that generates random lottery numbers given how many 'Quick Picks' are wanted"""
from random import randint


def main():
    valid_quickpick_number = False
    while not valid_quickpick_number:
        try:
            number_of_quickpicks = int(input("How many 'Quick Picks': "))
            valid_quickpick_number = True
        except ValueError:
            valid_quickpick_number = False
            print("Please enter a number!")
    generate_quickpicks(number_of_quickpicks)


def generate_quickpicks(number_of_quickpicks):
    for i in range(number_of_quickpicks):
        current_numbers = []
        NUMBER_1 = unique_random_number(current_numbers)
        NUMBER_2 = unique_random_number(current_numbers)
        NUMBER_3 = unique_random_number(current_numbers)
        NUMBER_4 = unique_random_number(current_numbers)
        NUMBER_5 = unique_random_number(current_numbers)
        NUMBER_6 = unique_random_number(current_numbers)
        print(
            "{:>3} {:>3} {:>3} {:>3} {:>3} {:>3}".format(
                NUMBER_1,
                NUMBER_2,
                NUMBER_3,
                NUMBER_4,
                NUMBER_5,
                NUMBER_6))


def unique_random_number(current_numbers):
    random_number = randint(1, 45)
    unique_number = False
    while not unique_number:
        number_in_list = False
        for current_number in current_numbers:
            if random_number == current_number:
                number_in_list = True
        if not number_in_list:
            unique_number = True
    return random_number


main()
