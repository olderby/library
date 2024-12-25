import library
import csv

def main():
    choice = menu()

    if choice == '5':
        print("Closing library!")
        return 0
    elif choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '8':
        add_library()
    elif choice == '9':
        add_book()
    else:
        menu()

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

def add_book():
    book_title = input("Enter book title:\t")
    book_author = input("Enter book author:\t")
    book_ISBN = input("Enter book ISBN:\t")
    book = library.Book(book_title, book_author, book_ISBN)
    with open('all_books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_title, book_author, book_ISBN])
    
def add_library():
    library_name = input("Enter a name for library collection:\t")
    

if __name__ == "__main__":
    main()