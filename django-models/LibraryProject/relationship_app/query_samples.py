from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

def query_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def query_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

# Example usage
if __name__ == "__main__":
    # Example queries (assuming data exists)
    try:
        books = query_all_books_by_author("John Doe")
        print("Books by John Doe:", [book.title for book in books])
        
        books_in_library = query_all_books_in_library("Central Library")
        print("Books in Central Library:", [book.title for book in books_in_library])
        
        librarian = query_librarian_for_library("Central Library")
        print("Librarian for Central Library:", librarian.name)
    except Author.DoesNotExist:
        print("Author not found.")
    except Library.DoesNotExist:
        print("Library not found.")
    except Librarian.DoesNotExist:
        print("Librarian not found.")
