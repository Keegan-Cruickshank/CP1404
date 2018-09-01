class ProgrammingLanguage:
    # Class holds Typing, Reflection, Year
    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self) -> bool:
        if self.typing == "Dynamic":
            return True
        else:
            return False


def run_tests():
    language1 = ProgrammingLanguage("Java", "Static", "Yes", 1995)
    language2 = ProgrammingLanguage("Python", "Dynamic", "Yes", 1991)
    print(language1.is_dynamic())
    print(language2.is_dynamic())


if __name__ == '__main__':
    run_tests()