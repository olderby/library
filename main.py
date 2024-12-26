from library import Book, Library
import csv

def main():

    choice = '0'

    saved_library = open_file()

    if saved_library == ' ':
        library = Library("Smithsonian")

    
    while choice != '5':
        choice = menu()
        if choice == '1':
            library.add_book()
        elif choice == '2':
            book_title = input("Enter book tittle to be borrowed:\t")
            library.borrow_book(book_title)
        elif choice == '3':
            library.return_book()
        elif choice == '4':
            library.list_books()
        else:
            print("Enter a valid option")

    print("Saving library...")
    with open('all_libraries.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(library)
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

def open_file():
    with open('all_libraries.csv', 'w', newline='') as file:
        return file

if __name__ == "__main__":
    main()