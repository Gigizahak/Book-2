from django.contrib import admin
from .models import Category, Author, Book

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)