"""
Assignment:
You've been tasked with writing the code for the wizard library. Complete the Library and Book classes listed below.

1. Create the Book Class:
    1. Create the __init__(self, title, author) method
    2. Set .title and .author to the values of the parameters.
2. Create the Library Class:
    1. Create the __init__(self, name) method
    2. Initialize a .name member variable to the value of the name parameter.
    3. Create a .books member initialized to an empty list.
3. Add the add_book(self, book) method:
    1. Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list.
4. Add the remove_book(self, book) method:
    1. Create a new, empty list to hold the books you want to keep.
    2. Loop through every book in the library's books list.
    3. If the book's title or author do not match the one you want to remove, add it to the new list.
    4. After checking all the books, replace the library's books list with the new list.
5. Add the search_books(self, search_string) method:
    1. For every book in the library check if the search_string is contained in the title or author field (case-insensitive).
    2. Return a list of all books that match the search string, ordered in the same order as they were added to the library.

After a book is removed, it should no longer be returned in the search results.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        books_to_keep = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                books_to_keep.append(b)
        self.books = books_to_keep

    def search_books(self, search_string):
        result_books = []
        for b in self.books:
            if (
                search_string.lower() in b.title.lower() 
                or search_string.lower() in b.author.lower()
               ):
                result_books.append(b)
        return result_books
