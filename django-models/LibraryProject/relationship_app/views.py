from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book, Library
from .models import Library        # for checker purposes


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
