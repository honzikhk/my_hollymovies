from django.urls import path
from books.views import BookHomepageView, BookListView, AuthorListView, BookDetailView, AuthorDetailView, \
    UpdateMovieView, UpdateAuthorView, CreateBookView, CreateAuthorView, DeleteBookView, DeleteAuthorView, \
    BookShelfListView, AddRemoveShelf

urlpatterns = (
    path('books_homepage/', BookHomepageView.as_view(), name='books_homepage'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('author_detail/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book_update/<int:pk>/', UpdateMovieView.as_view(), name='book_update'),
    path('author_update/<int:pk>/', UpdateAuthorView.as_view(), name='author_update'),
    path('book_create/', CreateBookView.as_view(), name='book_create'),
    path('author_create/', CreateAuthorView.as_view(), name='author_create'),
    path('book_confirm_delete/<int:pk>/', DeleteBookView.as_view(), name='book_confirm_delete'),
    path('author_confirm_delete/<int:pk>/', DeleteAuthorView.as_view(), name='author_confirm_delete'),
    path('book_shelf/', BookShelfListView.as_view(), name='book_shelf'),
    path('add_remove_shelf/<int:pk>/', AddRemoveShelf.as_view(), name="add_remove_shelf"),

)
