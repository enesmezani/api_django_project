from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Genre, Borrower, Transaction, Language, BookCopy, BookStatus, BookReview, Book, Publisher
from .serializers import AuthorSerializer, GenreSerializer, BorrowerSerializer, TransactionSerializer, LanguageSerializer, BookCopySerializer, BookStatusSerializer, BookReviewSerializer, BookSerializer, PublisherSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from .permission import adminPermission

# Create your views here.

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class AuthorViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (adminPermission, IsAuthenticated)
        
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class GenreViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (adminPermission, IsAuthenticated)

    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class BorrowerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class TransactionViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class LanguageViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (adminPermission, IsAuthenticated)
   
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class BookCopyViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class BookStatusViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = BookStatus.objects.all()
    serializer_class = BookStatusSerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class BookReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

    
class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (adminPermission, IsAuthenticated)
    
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)

class PublisherViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (adminPermission, IsAuthenticated)
   
    # def create(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, *args, **kwargs):
    #     if request.method == 'PUT':
    #         instance = self.get_object()
    #         serializer = self.get_serializer(instance, data=request.data, partial=True)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)
