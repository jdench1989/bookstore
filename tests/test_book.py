from lib.book import Book

def test_book_instantiates():
    book = Book(1, "Book title", "Book author")
    assert isinstance(book, Book)
    assert book.id == 1
    assert book.title == "Book title"
    assert book.author == "Book author"

def test_equal_if_properties_identical():
    book_1 = Book(1, "Book title", "Book author")
    book_2 = Book(1, "Book title", "Book author")
    assert book_1 == book_2

def test_formats_nicely_as_a_string():
    book = Book(1, "Book title", "Book author")
    assert str(book) == "Book(1, Book title, Book author)"