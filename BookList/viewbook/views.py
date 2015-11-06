from django.shortcuts import render
from django.views.generic import ListView
from viewbook.models import Book
from django.core.paginator import Paginator


class ViewListBook(ListView):
    model = Book
    paginate_by = 2
    # queryset = Book.objects.all()
    def get_queryset(self):
        return Book.objects.filter(id=1)

    def get_context_data(self, **kwargs):
        context = super(ViewListBook, self).get_context_data(**kwargs)
        return context
