from django.urls import path

from .views import (
    AuthorAPIView,
    BookApiView,
    AuthorAPIDetailView,
    BookApiDetailView,
)

urlpatterns = [
    path('author/', AuthorAPIView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorAPIDetailView.as_view(), name='author_detail'),
    # path('author/create/', AuthorAPICreateView.as_view(), name='author_create'),
    path('book/', BookApiView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookApiDetailView.as_view(), name='book_detail'),
]
