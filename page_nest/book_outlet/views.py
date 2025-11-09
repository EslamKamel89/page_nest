from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request: HttpRequest)->HttpResponse:
    books= Book.objects.all()
    return render(request , 'book_outlet/index.html' , {
        'books' : books ,
        'star_range' : range(5)
    })

def show(request:HttpRequest , id:int)->HttpResponse :
    book:Book = get_object_or_404(Book ,id=id)
    return render(request , 'book_outlet/book_detail.html', {
        'book'  : book ,
        'star_range' : 5
    })
