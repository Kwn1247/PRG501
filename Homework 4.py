# Homework 4
# Haixiang Yu
# 2025/5/30

class Book:
    def __init__(B, title, author, isbn):
        B.title = title
        B.author = author
        B.isbn = isbn
        B.borrowed = False

    def display_info(B):
        status = "Borrowed" if B.borrowed else "Available"
        print(f"Title: {B.title}, Author: {B.author}, ISBN: {B.isbn}, Status: {status}")


class Library:
    def __init__(B):
        B.books = []

    def add_book(B, book):
        B.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(B, title):
        for book in B.books:
            if book.title == title:
                B.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found.")

    def search_book(B, title):
        for book in B.books:
            if book.title.lower() == title.lower():
                book.display_info()
                return book
        print(f"Book '{title}' not found.")
        return None

    def list_books(B):
        if not B.books:
            print("No books in the library.")
        for book in B.books:
            book.display_info()


class Member:
    def __init__(B, name, membership_id):
        B.name = name
        B.membership_id = membership_id
        B.borrowed_books = []

    def borrow_book(B, library, book_title):
        book = library.search_book(book_title)
        if book and not book.borrowed:
            book.borrowed = True
            B.borrowed_books.append(book)
            print(f"{B.name} borrowed '{book.title}'.")
        elif book:
            print(f"'{book.title}' is currently borrowed by someone else.")

    def return_book(B, library, book_title):
        for book in B.borrowed_books:
            if book.title == book_title:
                book.borrowed = False
                B.borrowed_books.remove(book)
                print(f"{B.name} returned '{book.title}'.")
                return
        print(f"{B.name} did not borrow '{book_title}'.")


if __name__ == "__main__":
    library = Library()


    book1 = Book("Harry Potter and the Chamber of Secrets", "Rowling.J.K", "0001")
    book2 = Book("Harry Potter and the Sorcerer's Stone", "Rowling.J.K", "0002")
    book3 = Book("Dog Man", "Pilkey,Dav.", "0003")
    book4 = Book("The Essential Book of Succulents", "Kuroda, Kentaro.", "0004")


    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)


    print("\nLibrary Collection:")
    library.list_books()


    member1 = Member("James", "WU00001")
    member2 = Member("Chris", "WU00012")


    print("\nBorrowing Books:")
    member1.borrow_book(library, "Dog Man")
    member1.borrow_book(library, "Harry Potter and the Chamber of Secrets")

    print("\nLibrary Collection After Borrowing:")
    library.list_books()

    print("\nReturning Book:")
    member1.return_book(library, "Dog Man")

    print("\nLibrary Collection After Returning:")
    library.list_books()
