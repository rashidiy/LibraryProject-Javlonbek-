from os import getenv

from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import BooksForm, BooksUpdateForm
from .models import Books
# Create your views here.
def books_list_view(request):
    pass
    # books = Books.objects.all()
    # query= request.GET.get('query', '')
    # if query:
    #     books =[
    #         book for book in books
    #         if query.lower() in book.title.lower()
    #            #or query.lower() in book.category.lower()
    #            or query.lower() in book.author.lower()
    #     ]
    # context = {'books': books, 'query': query}
    # return render(request, 'book_list.html', context)

def books_detail_view(request, pk):
    pass
    # book = get_object_or_404(Books, pk=pk)
    # context = {'book': book}
    # return render(request, 'book_detail.html', context)

def books_create_view(request):
    pass
    # if request.method == "GET":
    #     form = BooksForm()
    #     context = {'form': form}
    #     return render(request, 'create_book.html', context)
    # if request.method == "POST":
    #     form = BooksForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         book = form.save()
    #         return redirect('/')
    #     context = {'form': form}
    #     return render(request, 'create_book.html', context)
    # return redirect('/')


def books_update_view(request, pk):
    pass
    # book = get_object_or_404(Books, pk=pk)
    # if request.method == "GET":
    #     form = BooksUpdateForm(instance=book)
    #     context = {'form': form}
    #     return render(request, 'update_book.html', context)
    # elif request.method == "POST":
    #     form = BooksUpdateForm(request.POST, instance=book)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('books-detail', pk=pk)
    #     context = {'form': form}
    #     return render(request, 'update_book.html', context)
    # else:
    #     return HttpResponseNotAllowed(['GET', 'POST'])

def books_delete_view(request, pk):
    pass
    # book = get_object_or_404(Books, pk=pk)
    # if request.method == "POST":
    #     book.delete()
    #     return redirect('/')
    # return render(request, 'book_delete.html', {'book': book})
