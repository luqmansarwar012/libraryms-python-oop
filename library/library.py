from book.book import Book
from utils.get_int_input import get_int_input


class Library:
    def __init__(self):
        self.members = {}
        self.books = {}

    def add_book(self, book):
        if book.book_id in self.books:
            self.books[book.book_id].copies_available += book.copies_available
        else:
            self.books[book.book_id] = book
            print(f"{book.title} By {book.author} added to library!.")

    def add_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member
            print(f"Member with '{member.name}' added!")

        else:
            print(f"Member with '{member.member_id}' alreaddy exits!")

    def issue_book(self):
        book_id = get_int_input("Enter 'book id'")
        member_id = get_int_input("Enter 'member id'")

        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book or not member:
            print("Invalid book id or member id")

        if book.copies_available > 0:
            member.books_borrowed.append(book)
            book.copies_available -= 1
            print(f"{book.title} issued to {member.name}")
        else:
            print("Sorry, the book is not available right now!")

    def return_book(self):
        book_id = get_int_input("Enter 'book id'")
        member_id = get_int_input("Enter 'member id'")

        book = self.books.get(book_id)
        member = self.members.get(member_id)

        if not book or not member:
            print("Invalid book id or member id")
        else:
            member.books_borrowed.remove(book)
            print(f"{member.name} has returned {book.title}")
            book.copies_available += 1

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(str(book))

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members.values():
            print(str(member))
