Book Store

1. Design and create the table
Table: books

Columns:
id | title | author_name

2. Test SQL seeds --> seeds/book_store.sql

3. Define class names
Model class
(in lib/book.py)
class Student

Repository class
(in lib/book_repository.py)
class BookRepository

4. Implement Model class

class Book:
    def __init__(self):
        self.id = 0
        self.title = title
        self.author_name = author_name


5. Define repository class interface

class BookRepository():
    def all():
        executes the SQL query:
        SELECT id, title, author_name FROM books
        returns an array of Book objects
        pass
        
    def find(id):
        executes the SQl query:
        SELECT id, title, author_name FROM books WHERE id = $1
        returns a single Book object

    def create(book):
        executes the SQL query:
        INSERT INTO books (title, author_name) VALUES([example title, example author name])
        returns None

    def delete(book):
        executes the SQL query:
        DELETE FROM books WHERE id = $1

6. Test examples
Model class:
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
    assert str(book) == "Book(1, Test Title, Author Name)"

"""
We can compare two identical books
and have them be equal
"""

def test_books_are_equal():
    book_1 = Book(1, "Test Title", "Test Author Name")
    book_2 = Book(1, "Test Title", "Test Author Name")
    assert book_1 == book_2

Repository Class:

"""
Get all books
"""
 def test_get_all_records(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    result = repository.all()
    assert result == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
    ]

Write a small program in app.py using the class BookRepository to print out the list of books to the terminal.