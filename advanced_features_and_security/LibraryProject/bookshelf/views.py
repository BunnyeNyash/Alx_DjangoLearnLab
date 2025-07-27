from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from .models import Book, Author
from django import forms
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle book creation logic
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        # Handle book edit logic
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})


class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)
    publication_year = forms.IntegerField()

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            author, _ = Author.objects.get_or_create(name=form.cleaned_data['author'])
            Book.objects.create(
                title=form.cleaned_data['title'],
                author=author,
                publication_year=form.cleaned_data['publication_year']
            )
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})
