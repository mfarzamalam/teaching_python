from django.urls import path
from .views import add_book


urlpatterns = [
    path("add/", add_book, name="add_book"),
    path("update/", add_book, name="update_book"),
    path("delete/", add_book, name="delete_book"),
]