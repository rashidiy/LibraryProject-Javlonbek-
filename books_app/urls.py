from django.urls import path
from .views import (books_list_view,
                    books_detail_view,
                    books_create_view, books_update_view, books_delete_view,
                     add_to_cart_ajax)

#
urlpatterns = [
     path('', books_list_view, name='home'),
     path('add-to-cart/', add_to_cart_ajax, name='add_to_cart_ajax'),
     path('book_detail/<int:pk>/', books_detail_view, name='books-detail'),
 ]