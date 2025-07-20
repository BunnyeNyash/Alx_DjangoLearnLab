# LibraryProject


## Repository Structure:
```
django-models/
    ├── LibraryProject/                # Django project directory
    │   ├── manage.py                 # Command-line utility for managing the project
    │   ├── README.md                 # Project-specific README
    |   ├── db.sqlite3
    |   ├── relationship_app/
    |    │   ├── __init__.py
    │   ├── admin.py
    |    │   ├── apps.py
    |    │   ├── migrations/
    |    │   ├── models.py
    |    │   ├── urls.py
    |    │   ├── views.py
    |    │   ├── query_samples.py
    |    │   └── templates/
    |    │       └── relationship_app/
    |    │           ├── list_books.html
    |    │           ├── library_detail.html
    |    │           ├── login.html
    |    │           ├── logout.html
    |    │           ├── register.html
    |    │           ├── admin_view.html
    |    │           ├── librarian_view.html
    |    │           ├── member_view.html
    |    ├── mysite/
    |    │   ├── __init__.py
    |    │   ├── settings.py
    |    │   ├── urls.py
    |    │   ├── wsgi.py
    |    ├── templates/
    |    │   ├── base.html
    |    │   └── registration/
    |    │       ├── login.html
    |    │       ├── signup.html
    |   |
    │   ├── LibraryProject/
    │   │   ├── __init__.py
    │   │   ├── settings.py          # Project settings and configurations
    │   │   ├── urls.py              # Project URL configuration
    │   │   ├── asgi.py
    │   │   ├── wsgi.py
    │   ├── bookshelf/                # Django app directory
    │   │   ├── __init__.py
    │   │   ├── admin.py             # Admin panel configuration
    │   │   ├── apps.py              # App configuration
    │   │   ├── migrations/
    │   │   │   ├── __init__.py
    │   │   ├── models.py            # Database models (Book model)
    │   │   ├── tests.py             # Test cases
    │   │   ├── views.py             # View logic
    │   │   ├── create.md            # Documentation for create operation
    │   │   ├── retrieve.md          # Documentation for retrieve operation
    │   │   ├── update.md            # Documentation for update operation
    │   │   ├── delete.md            # Documentation for delete operation
    │   │   ├── CRUD_operations.md   # Summary of CRUD operations
└── README.md
```
