import csv

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

    def __init__(self, name, books = [""]):
        self.name = name
        self.books = books

    #TODO: fix this function based on how we know the data is written to the csv file
    def open_library(self, file_name):
        books = []
        try:
            with open(file_name, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, author, isbn, is_borrowed = row
                    books.append(Book(title, author, isbn, is_borrowed == "True")) #TODO is_borrowed needs to be read from the file
        except FileNotFoundError:
            print(f"{file_name} not found. Starting with an empty library.")
        self.books = books
    
    #TODO: change this to rewrite the file, all library contents should be loaded and re written with updates each use
    def save_library(self, file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerows([[book.title, book.author, book.ISBN, book.is_borrowed]])
                # fixed issue of iterable items
                #TODO: encapsulate this in a to_list() function make it reusable

    def add_book(self, book):
        #add a book object to list of books
        self.books.append(book)

    #? borrow_book and return_book looks like the same method to me just to toggle a flag
    def borrow_book(self, title):
        for books in self.books:
            if books.title == title:
                books.is_borrowed = True

    def return_book(self, title):
        for books in self.books:
            if books.title == title:
                books.is_borrowed = False

    def list_books(self):
        #list all book objects by title in the list of book objects
        for books in self.books:
            print(books)

    def search(self, title):
        try:
            for books in self.books:
                if books.title == title:
                    print("I found the book!")
                    return True
        except:
            print("I cannot find that book")
            return False