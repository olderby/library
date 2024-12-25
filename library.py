class Book:
    author = "John Doe"
    is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} || {self.ISBN}"

    def __init__(self, title, author, ISBN, is_borrowed = False):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_borrowed = is_borrowed


class Library:

    def add_book(book):
        pass #add a book object to a list of book objects

    def borrow_book(title):
        pass #pop a book object out of the list of book objects

    def return_book(title):
        pass #insert a book object to the list of book objects

    def list_books():
        pass #list all book objects by title in the list of book objects

    def __init__(self, name, books = [""]):
        self.name = name
        self.books = books