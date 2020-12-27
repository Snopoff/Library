from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid


# Create your models here.


class Author(models.Model):
    """Model representing an author"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this author across whole library")
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    info = models.TextField(
        help_text="Brief information for this author", blank=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object"""
        return self.name


class Genre(models.Model):
    """Model representing genre"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this genre")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])


class Book(models.Model):
    """Model representing a book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this book across whole library")
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Brief description of the book", blank=True)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True)
    publish_year = models.DateField(null=True, blank=True)
    genre = models.ForeignKey(
        'Genre', on_delete=models.SET_NULL, null=True, default='2947d6ee-b0bf-439e-b869-e8bff3415576')

    class Meta:
        ordering = ['title', 'description']

    def get_absolute_url(self):
        """Returns the url to access a particular book instance"""
        return reverse('book-detail', args=[str(self.id)])
        # return reverse('book-detail', kwargs={'pk': str(self.id)})

    def __str__(self):
        """String for representing the Model object"""
        return self.title


class Order_Items(models.Model):
    """Model representing the items of an order"""
    order = models.ForeignKey(
        'Order', on_delete=models.SET_NULL, null=True)
    book = models.ManyToManyField(
        Book, help_text="Books in particular order")

    def get_books(self):
        return "\n".join([p.title for p in self.book.all()])

    def __str__(self):
        try:
            return "By 0{}:{}".format(self.order.visitor, self.get_books())
        except:
            return "None"


class Order(models.Model):
    """Model representing order"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for given order")
    visitor = models.ForeignKey(
        User, related_name='visitor', on_delete=models.SET_NULL, null=True, help_text="Visitor that made an order")
    staff = models.ForeignKey(
        User, related_name='staff', on_delete=models.SET_NULL, null=True, help_text="Staff that made an order")
    order_date = models.DateField(null=True)

    def __str__(self):
        return "{}: by {} on {}".format(self.id, self.visitor, self.order_date)

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False


# Comment this out due to the fact that I can create users by default
# Using django.contrib.auth.models.User
'''
class Visitor(models.Model):
    """Model representing a visitor"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for the visitor")
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    sex = models.BooleanField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('visitor-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Staff(models.Model):
    """Model representing staff"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for the staff person")
    name = models.CharField(max_length=100)
    sex = models.BooleanField(null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    birthday = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('staff-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
'''
