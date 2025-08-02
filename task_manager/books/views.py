from django.shortcuts import render

# Create your views here.

def add_book(request):
    context = {}
    return render(request, 'books/add_book.html', context)

