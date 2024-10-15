from book.book import Book
from .get_int_input import get_int_input


def create_book():
    id = get_int_input("Enter book id\n")
    title = input("Enter book title\n")
    author = input("Enter author\n")
    copies_available = get_int_input("Enter Number of copies\n")
    book = Book(id, title, author, copies_available)
    return book
