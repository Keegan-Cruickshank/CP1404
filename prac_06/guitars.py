from prac_06.guitar import Guitar


def main():
    guitars = loop_guitar_input()
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        print(
            "Guitar {}: {} ({}), worth ${:0,.2f}"
            .format(i + 1, guitar.name, guitar.year, guitar.cost),
            end=""
        )
        if guitar.is_vintage():
            print(" (vintage)")
        else:
            print("")


def loop_guitar_input() -> []:
    guitar_list = []
    while True:
        name = input("Name: ")
        if name.strip() != "":
            year = get_positive_int("Year: ", int)
            cost = get_positive_int("Cost: ", float)
            guitar = Guitar(name, year, cost)
            guitar_list.append(guitar)
        else:
            break
    return guitar_list


def get_positive_int(prompt, type):
    number = 0
    while number == 0 or number < 0:
        try:
            number = type(input(prompt))
            if number <= 0:
                print("Whoops, Needs to be a positive number")
        except ValueError:
            print("Whoops, Needs to be a number")
    return number


main()
