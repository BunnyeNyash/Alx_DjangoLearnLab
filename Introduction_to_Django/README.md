# Introduction to Django

## Django Development Environment, Models, and Admin Interface Project

This project introduces the fundamentals of Django, focusing on setting up a development environment, creating and managing models with the Django ORM, and utilizing the Django Admin interface. It is part of the `Alx_DjangoLearnLab` repository under the `Introduction_to_Django` directory.

### Repository

- GitHub: [Alx_DjangoLearnLab](https://github.com/BunnyeNyash/Alx_DjangoLearnLab.git)
- Directory: `Introduction_to_Django`

### Project Structure
```
Introduction_to_Django/
    ├── LibraryProject/                # Django project directory
    │   ├── manage.py                 # Command-line utility for managing the project
    │   ├── README.md                 # Project-specific README
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
    └── README.md                     # This file
```

### How to Use

1. **Clone the Repository** and navigate to `Introduction_to_Django/LibraryProject`:
   ```bash
   git clone https://github.com/BunnyeNyash/Alx_DjangoLearnLab.git
   cd Introduction_to_Django/LibraryProject
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

- **Task 0: Introduction to Django Development Environment Setup**
  - **Objective**: Set up a Django development environment and create a project named `LibraryProject`. Run the development server and explore the project structure.
  
- **Task 1: Implementing and Interacting with Django Models**
  - **Objective**: Create a `bookshelf` app, define a `Book` model with `title`, `author`, and `publication_year` fields, and perform CRUD operations using the Django ORM. Document each operation in separate Markdown files (`create.md`, `retrieve.md`, `update.md`, `delete.md`) and summarize in `CRUD_operations.md`.

- **Task 2: Utilizing the Django Admin Interface**
  - **Objective**: Register the `Book` model with the Django Admin interface, customize the admin display to show `title`, `author`, and `publication_year`, and add filters and search functionality for enhanced usability.
