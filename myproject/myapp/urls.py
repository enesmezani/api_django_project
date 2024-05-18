from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, GenreViewSet, BorrowerViewSet, TransactionViewSet, LanguageViewSet, BookCopyViewSet, BookStatusViewSet, BookReviewViewSet, BookViewSet, PublisherViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'borrowers', BorrowerViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'bookcopies', BookCopyViewSet)
router.register(r'bookstatuses', BookStatusViewSet)
router.register(r'bookreviews', BookReviewViewSet)
router.register(r'books', BookViewSet)
router.register(r'publishers', PublisherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
