class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return(
            "{} ({}) : ${:0,.2f}"
            .format(self.name, self.year, self.cost)
        )

    def get_age(self):
        return 2018 - self.year

    def is_vintage(self):
        if self.get_age() > 50:
            return True
        else:
            return False


def run_tests():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(guitar)


if __name__ == '__main__':
    run_tests()
