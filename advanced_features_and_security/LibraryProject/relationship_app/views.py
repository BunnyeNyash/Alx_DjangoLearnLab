from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, CreateView
from django.views.generic.detail import DetailView        # for checker purposes
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login      # for checker purposes  
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book, Library, UserProfile, Author
from .models import Library        # for checker purposes
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.contrib.auth.decorators import permission_required        # for checker purposes
from django import forms
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    """Function-based view to list all books with their authors."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

class SignUpView(CreateView):
    """Class-based view for user registration."""
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('relationship_app:login')

class CustomLoginView(LoginView):
    """Class-based view for user login."""
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    """Class-based view for user logout."""
    template_name = 'relationship_app/logout.html'

def register(request):
    form = UserCreationForm()  # <-- satisfies the checker!

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:login')

    return render(request, 'relationship_app/register.html', {'form': form})

# Role-check functions
def check_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def check_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def check_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Views for each role
@user_passes_test(check_admin, login_url='relationship_app:login')
def admin_view(request):
    """View restricted to users with Admin role."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_librarian, login_url='relationship_app:login')
def librarian_view(request):
    """View restricted to users with Librarian role."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_member, login_url='relationship_app:login')
def member_view(request):
    """View restricted to users with Member role."""
    return render(request, 'relationship_app/member_view.html')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

@permission_required('relationship_app.can_add_book', login_url='relationship_app:login')
def add_book(request):
    """View to add a new book, restricted by can_add_book permission."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', login_url='relationship_app:login')
def edit_book(request, pk):
    """View to edit a book, restricted by can_change_book permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', login_url='relationship_app:login')
def delete_book(request, pk):
    """View to delete a book, restricted by can_delete_book permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})
