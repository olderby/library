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

    books = []

    def add_book(self, book):
        #add a book object to a list of book objects
        book_title = input("Enter book title:\t")
        book_author = input("Enter book author:\t")
        book_ISBN = input("Enter book ISBN:\t")
        book = Book(book_title, book_author, book_ISBN)
        self.books.append(book)

    def borrow_book(self, title):
        #if the title is in the library mark it as borrorwed
        try:
            for books in self.books:
                if books.title == title:
                    print("I found the book!")
        except:
            print("I cannot find that book")

    def return_book(title):
        pass #insert a book object to the list of book objects

    def list_books(self):
        #list all book objects by title in the list of book objects
        for books in self.books:
            print(books)

    def __init__(self, name, books = [""]):
        self.name = name
        self.books = books
