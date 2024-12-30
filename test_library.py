from main import Library, Book
import unittest


file_name = 'test_all_books.csv'

#* testing adding a book and it appears in the list of books
class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        test_library = Library("test_library_add_book")
        test_book = ["The simple book", "John Smith", "123-1-12345-123-1", False]

        test_library.add_book(test_book)

        # Check multiple aspects of add_book in one test
        assert len(test_library.books) == 1, "Book count mismatch"
        assert test_library.books[0].title == "The simple book", "Title mismatch"
        assert test_library.books[0].author == "John Smith", "Author mismatch"
        assert test_library.books[0].ISBN == "123-1-12345-123-1", "ISBN mismatch"
        assert test_library.books[0].is_borrowed == False, "Borrowed status mismatch"

#* tests that borrowing a book changes the is_borrowed flag to True
def test_borrow_book():
    pass

#* tests that return a book changes the is_borrowed flag to False
def test_return_book():
    pass

#* tests that searching for abook by title returns the correct response
def test_search_book():
    pass


#* tests that books are saved and loaded without data loss
def test_save_load_books():
    pass
