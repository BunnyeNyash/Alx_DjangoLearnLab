from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return author

    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        if year < 0 or year > 2025:
            raise forms.ValidationError("Publication year must be between 0 and 2025.")
        return year
