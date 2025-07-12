# Create Operation
**Command**:
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```

**Expected Output:**
```
Successfully created a Book instance with title "1984", author "George Orwell", and publication_year 1949.
```
