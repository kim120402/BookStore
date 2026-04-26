from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/',
        '/api/books/',
        '/api/books/<id>/',
    ]

    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()  # get all books
    serializer = BookSerializer(books, many=True)  # convert books to JSON

    return Response(serializer.data)


@api_view(['GET'])
def getBook(request, bookId):
    book = get_object_or_404(Book, id=bookId)  # get book by id or show 404
    serializer = BookSerializer(book, many=False)  # convert one book to JSON

    return Response(serializer.data)