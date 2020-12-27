from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<str:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<str:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genre/<str:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
]

# Borrowed books
urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url(r'^givenbooks/$', views.GivenBooksByStaffListView.as_view(), name='my-given')
]
