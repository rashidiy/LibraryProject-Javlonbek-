from django.shortcuts import render

# Create your views here.
def books_list_view(request):
    return render(request, 'index.html')

def books_detail_view(request):
    return render(request, 'book_detail.html')

def books_create_view(request):
    pass


def books_update_view(request, pk):
    pass

def books_delete_view(request, pk):
    pass
