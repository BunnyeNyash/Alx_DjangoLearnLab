# Django Models

## Deep Dive into Django Models and Views

This project is meant to solidify understanding of Django’s ORM capabilities, view configurations, and user authentication features. There is the implementation of complex model relationships, development of both function-based and class-based views, and management of user authentication and permissions. It is part of the `Alx_DjangoLearnLab` repository under the `django-models` directory.

### Repository

- GitHub: [Alx_DjangoLearnLab](https://github.com/BunnyeNyash/Alx_DjangoLearnLab.git)
- Directory: `django-models`

### Project Structure
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

### How to Use

1. **Clone the Repository** and navigate to `django-models`:
   ```bash
   git clone https://github.com/BunnyeNyash/Alx_DjangoLearnLab.git
   cd django-models
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install and Save Dependencies**:
   ```bash
   pip install django
   pip freeze > requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations bookshelf
   python manage.py migrate
   ```

5. **Create a Superuser (Admin User) for Testing**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Visit `http://127.0.0.1:8000/admin/` and log in to verify the setup and access the admin interface.

### Tasks

- **Task 0**: Implement advanced model relationships (`ForeignKey`, `ManyToMany`, `OneToOne`) and create a `query_samples.py` script.
- **Task 1**: Create function-based and class-based views, configure URL patterns, and provide templates.
- **Task 2**: Set up user authentication with login, logout, and registration.
- **Task 3**: Implement role-based access control with a UserProfile model and role-specific views.
- **Task 4**: Add custom permissions to the Book model and secure views with permission checks.
