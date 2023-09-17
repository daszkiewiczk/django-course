from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min

def index(request):
    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aggregate()

    return render(request, 'bookoutlet/index.html', {
        'books': books,
        'total_number_of_books': books.count(),
        'average_rating': books.aggregate(Avg('rating'))
    })


def book_detail(request, slug):
    # try:
    #     book = Book.book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'bookoutlet/book_detail.html', {
        'title': book.title,
        'is_bestseller': book.is_bestselling,
        'rating': book.rating,
        'author': book.author,
    })