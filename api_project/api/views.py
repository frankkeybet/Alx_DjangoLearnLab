from django.shortcuts import render
from rest_framework import generics, viewsets
#from rest_framework.viewsets import ApiView
from .models import Book
from .serializers import BookSerializer



# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        