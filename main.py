from library import Book, Library
import csv

def main():

    choice = '0' #? Can i run a while without initializing this?
    file_name = 'all_books.csv'

    #Abandon the idea of multiple libraries this project will be just one library per instance
    library = Library("Smithsonian")
    library.open_library(file_name)

    
    while choice != '5':
        choice = menu()
        if choice == '1': #?seems a bit overcomplicated to me but goal is to be modular?
            book = make_book()
            library.add_book(book)
        elif choice == '2':
            book_title = input("Enter book title to be borrowed:\t")
            if library.search(book_title):
                library.borrow_book(book_title)
        elif choice == '3':
            book_title = input("Enter book title to be returned:\t")
            if library.search(book_title):
                library.return_book(book_title)
        elif choice == '4':
            library.list_books()
        else:
            print("Enter a valid option")

    print("Saving library...")
    library.save_library(file_name)
    print("Exiting Program")

def menu():
    print("** Electronic Library system **")
    print("Options: ")
    print("1. Add a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. List all books")
    print("5. Exit")
    choice = input('')
    return choice

def make_book():
    book_title = input("Enter book title:\t")
    book_author = input("Enter book author:\t")
    book_ISBN = input("Enter book ISBN:\t")
    book = Book(book_title, book_author, book_ISBN)
    return book

if __name__ == "__main__":
    main()