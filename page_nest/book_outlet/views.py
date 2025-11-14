from __future__ import annotations

from django.db.models import Avg
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book


def index(request: HttpRequest)->HttpResponse:
    books= Book.objects.all().order_by('-rating')
    average_rating = books.aggregate(Avg('rating'))['rating__avg']
    total_count = books.count()
    return render(request , 'book_outlet/index.html' , {
        'books' : books ,
        'star_range' : range(5) ,
        'average_rating' : round(average_rating , 2) ,
        'total_count' : total_count ,
    })

def show(request:HttpRequest , slug:str)->HttpResponse :
    book:Book = get_object_or_404(Book ,slug=slug)
    return render(request , 'book_outlet/book_detail.html', {
        'book'  : book ,
        'countries' : book.published_countries.all() , # type: ignore
        'star_range' : 5
    })
