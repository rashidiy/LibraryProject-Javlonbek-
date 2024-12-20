from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ReviewCreateForm, OrderForm
from .models import Books, Reviews, Category, Cart, OrderItem



# Create your views here.
def books_list_view(request):
    categories = Category.objects.all()
    last_books = Books.objects.filter(availability='On sale').order_by('-average_rating')[:10]
    books = Books.objects.filter(availability='On sale').order_by('-id')[:8]
    featured_books = Books.objects.filter(average_rating__gte=4, average_rating__lte=5, availability='On sale').order_by('-average_rating')[:4]
    query = request.GET.get("query", "")
    if query:
        books = [
            book for book in books
            if query.lower() in book.title.lower()
               or query.lower() in book.category.lower()
               or query.lower() in book.price.lower()
        ]

    context = {'last_books': last_books,
               'books': books,
               'featured_books': featured_books,
               'categories': categories,
               'query': query}
    return render(request, 'index.html', context)

@login_required
def books_detail_view(request, pk):
    review_form = None
    book = get_object_or_404(Books, pk=pk)
    categories = book.category.all()
    reviews = Reviews.objects.filter(book=book).order_by('-created_at')
    if request.method=='POST':
        review_form = ReviewCreateForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
    context = {'book': book,
               'reviews':reviews,
               'categories': categories,
               'review_form':review_form,
               }
    return render(request, 'book_detail.html', context)


@login_required
def add_to_cart_ajax(request):
    if request.method == 'POST' and request.user.is_authenticated:
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Books, pk=book_id)
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
        order, created_order = OrderItem.objects.get_or_create(book=book)
        if cart.orders.filter(id=order.id).exists():
            cart.orders.remove(order)
            return JsonResponse({'message': '-----  Book removed from cart  -----', 'status': 'success'})
        else:
            cart.orders.add(order)
            return JsonResponse({'message': 'Book added to cart successfully!', 'status': 'success'})

    return JsonResponse({'message': 'Invalid request', 'status': 'error'})



@login_required
def cart_detail_view(request, pk):
    cart = Cart.objects.get(pk=pk)
    pass

def books_create_view(request):
    pass


def books_update_view(request, pk):
    pass

def books_delete_view(request, pk):
    pass
