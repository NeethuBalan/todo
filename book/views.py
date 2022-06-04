from django.shortcuts import render,redirect
from book.forms import BookForm
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from book.models import Books
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book-add.html'
    success_url = reverse_lazy('list-book')

class BookListView(ListView):
    model = Books
    template_name = 'book-list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"

class BookEditView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = 'book-edit.html'
    success_url = reverse_lazy('list-book')
    pk_url_kwarg = "id"

def bookdelete(request,*args,**kwargs):
    id=kwargs.get('id')
    Books.objects.get(id=id).delete()
    return redirect('list-book')