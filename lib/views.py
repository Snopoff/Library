from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from datetime import date, timedelta
from .models import *

paginator = 30


class BookListView(generic.ListView):
    model = Book
    paginate_by = paginator

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(title__icontains=query)
        else:
            return Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['book_list'] = Book.objects.all()
        book_id = self.request.get_full_path().split('/')[-1]
        b = Book.objects.filter(id=book_id)[0]
        try:
            user_id = Order_Items.objects.filter(book=b).values(
                'order__visitor').order_by('order__order_date')[0]['order__visitor']
            data['last_user'] = User.objects.filter(id=user_id)[0]
        except:
            data['last_user'] = 'None'

        return data


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = paginator

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Author.objects.filter(name__icontains=query)
        else:
            return Author.objects.all()


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = Order_Items
    template_name = 'lib/book_list_borrowed_user.html'
    paginate_by = paginator

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        books = Order_Items.objects.filter(order__visitor=self.request.user).values(
            'book').order_by('order__order_date')
        data['book_list'] = Book.objects.filter(id__in=books)
        data['order_date'] = Order_Items.objects.filter(order__visitor=self.request.user).values(
            'order__order_date')[0]['order__order_date']
        data['order_date_str'] = data['order_date'].strftime('%m.%d.%Y')
        data['is_overdue'] = data['order_date'] + \
            timedelta(days=14) < date.today()
        print(data['is_overdue'])

        return data

    '''
    def get_queryset(self):
        books = Order_Items.objects.filter(order__visitor=self.request.user).values(
            'book').order_by('order__order_date')

        return Book.objects.filter(id__in=books)
    '''


class GivenBooksByStaffListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on given books by current staff user.
    """
    model = Order_Items
    template_name = 'lib/book_list_borrowed_user.html'
    paginate_by = paginator

    def get_queryset(self):
        books = Order_Items.objects.filter(order__staff=self.request.user).values(
            'book').order_by('order__order_date')

        return Book.objects.filter(id__in=books)


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 30

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Genre.objects.filter(name__icontains=query)
        else:
            return Genre.objects.all()


class GenreDetailView(generic.DetailView):
    model = Genre


def index(request):
    """View homepage"""
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_authors': num_authors,
                 'num_visits': num_visits, }
    )
