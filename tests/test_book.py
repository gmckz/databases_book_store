from lib.book import Book

"""
Book constructs with an id, title and author name
"""
def test_book_constructs():
    book = Book(1, "Test Title", "Test Author Name")
    assert book.id == 1
    assert book.title == "Test Title"
    assert book.author_name == "Test Author Name"

"""
We can format books into strings nicely
"""

def test_books_format_nicely():
    book = Book(1, "Test Title", "Test Author Name")
    assert str(book) == "Book(1, Test Title, Test Author Name)"

"""
We can compare two identical books
and have them be equal
"""

def test_books_are_equal():
    book_1 = Book(1, "Test Title", "Test Author Name")
    book_2 = Book(1, "Test Title", "Test Author Name")
    assert book_1 == book_2