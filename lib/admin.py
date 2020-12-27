from django.contrib import admin

# Register your models here.
from .models import Author, Book, Order_Items, Order, Genre  # , Staff, Visitor


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'info')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'genre', 'publish_year')


@admin.register(Order_Items)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'get_books')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'staff', 'order_date')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
