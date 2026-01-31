from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet
#from rest_framework.viewsets import ApiView
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticatedOrReadOnly





# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        #permission_classes = [IsAuthenticated]
        permission_classes = [IsAuthenticatedOrReadOnly]


        
class AdminBookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]