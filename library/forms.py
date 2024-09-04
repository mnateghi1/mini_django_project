from django import forms

from library.models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'price',
            'description',
            'genre',
            'number_of_pages',
        ]

class SearchForm(forms.Form):
    query = forms.CharField()