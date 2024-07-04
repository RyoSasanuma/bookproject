from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'isbn_code',
            'title',
            'authors',
            'publisher', 
            'published_date', 
            'description', 
            'page_count', 
            'categories', 
            'average_rating', 
            'ratings_count', 
            'small_thumbnail', 
            'thumbnail', 
            'language'
            ]