"""
Keegan Cruickshank
CP1404
Book reading tracker that keeps track of the books you want to read and the ones you already have.

"""

FILE_NAME = "books.csv"


def main():
    input_file = open(FILE_NAME, "r")
    books = input_file.readlines()
    number_of_lines = len(books)
    input_file.close()
    formatted_books = []
    for book in books:
        formatted_book = book.strip().split(",")
        formatted_books.append(formatted_book)
    print("Reading Tracker 1.0 - by Keegan Cruickshank")
    print("{} books loaded from {}".format(number_of_lines, FILE_NAME))
    show_menu(formatted_books)


def show_menu(books):
    print("Menu:")
    print("L - List all books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    user_menu_input = input(">>>")
    if selection_is_valid(user_menu_input):
        select_menu_item(user_menu_input.upper(), books)
    else:
        print("Invalid menu choice")
        show_menu()


def select_menu_item(menu_item, books):
    if menu_item == "L":
        list_all_books(books)
    elif menu_item == "A":
        add_new_book(books)
    elif menu_item == "M":
        mark_book_as_complete(books)
    else:
        quit_application(books)


def selection_is_valid(user_menu_input) -> bool:
    uppercase_menu_input = user_menu_input.upper()
    if uppercase_menu_input in ["L", "A", "M", "Q"]:
        return True
    else:
        return False


def list_all_books(books):
    book_name_char_required = get_max_name_length(books) + 1
    book_author_char_required = get_max_author_length(books) + 1
    for i, book in enumerate(books):
        if is_completed(book):
            print(" {}. {name:<{name_space}}by {author:<{author_space}}{pages:>4} pages".format(i + 1, name_space=book_name_char_required, author_space = book_author_char_required, name=book[0], author=book[1], pages=book[2]))
        else:
            print("*{}. {name:<{name_space}}by {author:<{author_space}}{pages:>4} pages".format(i + 1, name_space=book_name_char_required, author_space = book_author_char_required, name=book[0], author=book[1], pages=book[2]))
    print("{} books.".format(len(books)))
    print("You need to read {} pages in {} books".format(get_unread_pages(books), get_unread_books(books)))
    show_menu(books)


def get_unread_pages(books):
    unread_pages = 0
    for book in books:
        if book[3] == "r":
            unread_pages += int(book[2])
    return unread_pages


def get_unread_books(books):
    unread_books = 0
    for book in books:
        if book[3] == "r":
            unread_books += 1
    return unread_books


def get_max_name_length(books):
    current_max_length_name = 0
    for book in books:
        length_of_name = len(book[0])
        if length_of_name > current_max_length_name:
            current_max_length_name = length_of_name
    return current_max_length_name


def get_max_author_length(books):
    current_max_length_author = 0
    for book in books:
        length_of_author = len(book[1])
        if length_of_author > current_max_length_author:
            current_max_length_author = length_of_author
    return current_max_length_author


def is_completed(book):
    if book[3] == 'r':
        return False
    else:
        return True


def add_new_book(books):
    print("Adding Book")
    show_menu(books)


def mark_book_as_complete(books):
    print("Mark Book Complete")
    show_menu(books)


def quit_application(books):
    print("{} books have been saved to {}".format(len(books), FILE_NAME))
    print("Have a nice day :)")
    quit()


main()
