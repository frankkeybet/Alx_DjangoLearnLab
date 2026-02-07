# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book , Author


class BookAPITestCase(APITestCase):

    def setUp(self):
       # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create authors
        self.author1 = Author.objects.create(name="Author A")
        self.author2 = Author.objects.create(name="Author B")

        # Create books using Author instances
        self.book1 = Book.objects.create(
            title="Book One",
            author=self.author1.id,  
            published_date="2020-01-01",
            isbn="1234567890123"
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author=self.author2.id,  
            published_date="2021-06-15",
            isbn="1234567890124"
        )

        # API client
        self.client = APIClient()
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')


    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # two books created in setUp

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)


    def test_create_book_authenticated(self):
        """Test creating a book as an authenticated user"""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Book Three",
            "author": "Author C",
            "published_date": "2022-03-10",
            "isbn": "1234567890125"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="Book Three").author, "Author C")

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book"""
        data = {
            "title": "Book Four",
            "author": "Author D",
            "published_date": "2022-07-10",
            "isbn": "1234567890126"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book(self):
        """Test updating a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {"title": "Updated Book One"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")


    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())


    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.list_url, {'author': 'Author A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author A')

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {'search': 'Two'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_order_books(self):
        """Test ordering books by published_date descending"""
        response = self.client.get(self.list_url, {'ordering': '-published_date'})
        self.assertEqual(response.data[0]['published_date'], '2021-06-15')


