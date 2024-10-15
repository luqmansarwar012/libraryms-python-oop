from library.library import Library
from utils.get_int_input import get_int_input
from utils.book_utils import create_book
from utils.member_utils import create_member


def main():
    library = Library()
    menu = """
           *****  Library Management System  *****\n
           1. Add a book.\n
           2. Add a member.\n
           3. Issue a book to member.\n
           4. Book return.\n
           5. Display books.\n
           6. Display members.\n
           7. Exit.
            """

    while True:
        print(menu)
        choice = get_int_input("Enter your choice: ")
        match int(choice):
            case 1:
                book = create_book()
                library.add_book(book)
            case 2:
                member = create_member()
                library.add_member(member)
            case 3:
                library.issue_book()
            case 4:
                library.return_book()
            case 5:
                library.display_books()
            case 6:
                library.display_members()
            case 7:
                break


if __name__ == "__main__":
    main()
