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
        show_menu(books)


def select_menu_item(menu_item, books):
    if menu_item == "L":
        list_all_books(books)
        show_menu(books)
    elif menu_item == "A":
        add_new_book(books)
        show_menu(books)
    elif menu_item == "M":
        mark_book_as_complete(books)
        show_menu(books)
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
    if all_books_are_completed(books):
        print("No books left to read. Why not add a new book?")
    else:
        print("You need to read {} pages in {} books".format(get_unread_pages(books), get_unread_books(books)))


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
    book_title = input("Title: ")
    while book_title.strip() == "":
        print("Input can not be blank")
        book_title = input("Title: ")
    book_author = input("Author: ")
    while book_author.strip() == "":
        print("Input can not be blank")
        book_author = input("Author: ")
    book_pages = input("Pages: ")
    while not valid_positive_int(book_pages)[0]:
        print(valid_positive_int(book_pages)[1])
        book_pages = input("Pages: ")
    new_book_object = [book_title, book_author, book_pages, "r"]
    books.append(new_book_object)
    output_file = open(FILE_NAME, 'w')
    for book in books:
        output_file.write("{},{},{},{}\n".format(book[0], book[1], book[2], book[3]))
    print("{} by {}, ({} pages) added to Reading Tracker".format(book[0], book[1], book[2]))


def valid_positive_int(potential_number):
    response = []
    try:
        number = int(potential_number)
        if number > 0:
            response.append(True)
        else:
            response.append(False)
            response.append("Number must be > 0")
    except ValueError:
        response.append(False)
        response.append("Invalid input; enter a valid number")
    return response


def mark_book_as_complete(books):
    if not all_books_are_completed(books):
        list_all_books(books)
        user_input = get_book_to_mark_as_complete(books)
        book_index = user_input - 1
        if books[book_index][3] == "c":
            print("That book is already completed")
        else:
            books[book_index][3] = "c"
            output_file = open(FILE_NAME, "w")
            for book in books:
                output_file.write("{},{},{},{}\n".format(book[0], book[1], book[2], book[3]))
            print("{} by {} completed!".format(books[book_index][0], books[book_index][1]))
    else:
        print("No required books")


def all_books_are_completed(books):
    all_books_completed = True
    for book in books:
        if book[3] == "r":
            all_books_completed = False
    return all_books_completed


def get_book_to_mark_as_complete(books) -> int:
    print("Enter the number of a book to mark as completed")
    user_input = input(">>>")
    valid_input = False
    while not valid_input:
        try:
            selection_number = int(user_input)
            if selection_number <= 0:
                print("Number must be > 0")
                user_input = input(">>>")
            elif selection_number > len(books):
                print("Invalid book number")
                user_input = input(">>>")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
            user_input = input(">>>")
    return int(user_input)


def quit_application(books):
    print("{} books have been saved to {}".format(len(books), FILE_NAME))
    print("Have a nice day :)")
    quit()


main()
