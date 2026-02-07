from django.shortcuts import render
from rest_framework import generics, permissions,filters
from .models import Book
from .serializers import BookSerializer ,AuthorSerializer
from rest_framework.permissions import BasePermission

# Create your views here.

class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff


# List all books (GET)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

# Retrieve single book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book (POST)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # only logged in users

    def perform_create(self, serializer):
        isbn = serializer.validated_data.get('isbn')
        if len(isbn) != 13:
            raise serializers.ValidationError("ISBN must be 13 characters")
        serializer.save()

# Update existing book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
   # permission_classes = [permissions.IsAuthenticated]
