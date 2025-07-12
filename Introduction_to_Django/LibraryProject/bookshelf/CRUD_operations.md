# CRUD Operations Documentation

## 1. Create
**Command**:
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

**Output:** Successfully created a Book instance.

## 2. Retrieve
**Command**:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

**Output:** 1984 George Orwell 1949

## 3. Update
**Command**:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

**Output:** Nineteen Eighty-Four

## 4. Delete
**Command**:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
```

**Output:** <QuerySet []>
