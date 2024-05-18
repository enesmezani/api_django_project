from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Genre, Borrower, Transaction, Language, BookCopy, BookStatus, BookReview, Book, Publisher
from .serializers import AuthorSerializer, GenreSerializer, BorrowerSerializer, TransactionSerializer, LanguageSerializer, BookCopySerializer, BookStatusSerializer, BookReviewSerializer, BookSerializer, PublisherSerializer

# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class BookCopyViewSet(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer

class BookStatusViewSet(viewsets.ModelViewSet):
    queryset = BookStatus.objects.all()
    serializer_class = BookStatusSerializer

class BookReviewViewSet(viewsets.ModelViewSet):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

