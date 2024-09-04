from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>', views.book_detail, name='book_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('search/', views.search_book, name='search_book'),
    path('delete_book/<int:id>', views.delete_book, name='delete_book'),
]
