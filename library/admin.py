from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'user',
        'price',
        'published',
        'status',
    ]
    ordering = [
        'title',
        'published',
    ]
    list_filter = [
        'price',
        'published',
    ]
    search_fields = [
        'title',
        'author',
    ]
    # raw_id_fields = ['author']
    prepopulated_fields = {'slug' : ['title']}
    list_editable = [
        'status',
    ]
