from django.urls import path
from .views import books_list_view, books_detail_view, books_create_view, books_update_view, books_delete_view
#
urlpatterns = [
     path('', books_list_view, name='books-list'),
     path('book_detail/', books_detail_view, name='books-detail'),
 ]