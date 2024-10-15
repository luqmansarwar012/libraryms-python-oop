class Book:
    def __init__(self, book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def __str__(self):
        return f"book_id: {self.book_id}, title: {self.title}, author: {self.author}, copies_available: {self.copies_available}"
