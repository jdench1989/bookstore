from lib.book import Book

class BookRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for dictionary in rows:
            book = Book(dictionary['id'], dictionary['title'], dictionary['author_name'])
            books.append(book)
        return books