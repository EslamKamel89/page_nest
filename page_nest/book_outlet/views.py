from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Book


def index(request: HttpRequest)->HttpResponse:
    books= Book.objects.all()
    return render(request , 'book_outlet/index.html' , {
        'books' : books ,
        'star_range' : range(5)
    })
