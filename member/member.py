class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.books_borrowed = []

    def __str__(self):
        return f"member_id: {self.member_id}, name: {self.name}, books_borrowed:{self.books_borrowed}"
