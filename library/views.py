from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.defaultfilters import title

from .models import Book
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'library/index.html')

def book_list(request):
    books = Book.publish.all()
    context = {
        'books': books,
    }
    return render(request, 'library/list.html', context)

def book_detail(request, id):
    try:
        book = Book.publish.get(id=id)
    except:
        raise Http404('Book not found')
    context = {
        'book': book,
    }
    return render(request, 'library/detail.html', context)

def add_book(request):
    if request.method == "POST":
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('library:index')
    else:
        form = AddBookForm()
    return render(request, 'forms/add_book.html', {'form': form})

def search_book(request):
    query=None
    results = []
    if "query" in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results1 = Book.publish.filter(title__icontains=query)
            results2 = Book.publish.filter(author__icontains=query)
            results = results1 | results2
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'library/search.html', context)

def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('library:index')
    return render(request, 'forms/delete_book.html', {'book': book})