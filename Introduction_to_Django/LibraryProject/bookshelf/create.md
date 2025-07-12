# Create Operation
**Command**:
```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

**Expected Output:**
```
Successfully created a Book instance with title "1984", author "George Orwell", and publication_year 1949.
```
