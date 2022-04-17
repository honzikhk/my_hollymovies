from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from books.models import Book, Author
from books.forms import BookForm, AuthorForm


class BooksDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super(BooksDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class BookDetailView(BooksDetailView):
    model = Book
    template_name = 'book_detail.html'

    def post(self, request, pk, *args, **kwargs):
        book = self.get_object()
        book.likes += 1
        book.save(update_fields=['likes', ])
        return redirect('book_detail', pk=pk)


class AddRemoveShelf(DetailView):
    model = Book
    template_name = "books.html"

    def post(self, request, pk, *args, **kwargs):
        book = self.get_object()
        if not book.on_shelf:
            book.on_shelf = True
            book.save(update_fields=['on_shelf', ])
            return redirect('books', )
        else:
            book.on_shelf = False
            book.save(update_fields=['on_shelf', ])
            return redirect('books', )


class AuthorDetailView(BooksDetailView):
    model = Author
    template_name = 'author_detail.html'


class BookHomepageView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'number_of_books': Book.objects.all().count(),
            'number_of_authors': Author.objects.all().count(),
            'page_name': 'Books homepage'
        }
        return TemplateResponse(request, 'books_homepage.html', context=context)


class BookListView(ListView):
    queryset = Book.objects.all().order_by('-rating')
    template_name = 'books.html'
    extra_context = {'page_name': 'Books'}


class AuthorListView(ListView):
    queryset = Author.objects.all()
    template_name = 'authors.html'
    extra_context = {'page_name': 'Authors'}


class UpdateMovieView(UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book
    extra_context = {'page_name': 'Update book'}


class UpdateAuthorView(UpdateView):
    template_name = "author_update.html"
    form_class = AuthorForm
    model = Author
    extra_context = {"page_name": "Update author"}


class CreateBookView(CreateView):
    template_name = "book_create.html"
    form_class = BookForm
    model = Book
    extra_context = {'page_name': 'Create book'}


class CreateAuthorView(CreateView):
    template_name = "author_create.html"
    form_class = AuthorForm
    model = Author
    extra_context = {'page_name': 'Create author'}


class DeleteBookView(DeleteView):
    template_name = 'book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('books')
    extra_context = {'page_name': 'Delete book'}


class DeleteAuthorView(DeleteView):
    template_name = "author_confirm_delete.html"
    model = Author
    success_url = reverse_lazy("authors")
    extra_context = {"page_name": "Delete author"}


class BookShelfListView(ListView):
    queryset = Book.objects.filter(on_shelf=True)
    template_name = "book_shelf.html"
    extra_context = {'page_name': 'Book shelf'}







