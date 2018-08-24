def main():
    """Get 5 random numbers from user."""
    numbers = []
    for index in range(5):
        valid = False
        while not valid:
            try:
                numbers.append(int(input("Number: ")))
                valid = True
            except ValueError:
                valid = False
                print("Please enter a number!")

    print_random(numbers)


def print_random(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    numbers.sort()
    print("The smallest number is {}".format(numbers[0]))
    print("The largest number is {}".format(numbers[-1]))
    added_numbers = 0
    for number in numbers:
        added_numbers += number
    average = added_numbers / len(numbers)
    print("The average of the numbers is {}".format(average))


main()