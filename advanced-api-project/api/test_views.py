from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from api.models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Create authors
        self.author1 = Author.objects.create(name="Author A")
        self.author2 = Author.objects.create(name="Author B")

        # Create books
        self.book1 = Book.objects.create(
            title="Book One",
            publication_year=2020,
            author=self.author1
        )

        self.book2 = Book.objects.create(
            title="Book Two",
            publication_year=2021,
            author=self.author2
        )

        # API client
        self.client = APIClient()

        # URLs
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")

    # ----------------------------
    # LIST + DETAIL TESTS
    # ----------------------------
    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving one book by ID"""
        url = reverse("book-detail", kwargs={"pk": self.book1.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # ----------------------------
    # CREATE TESTS
    # ----------------------------
    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "Book Three",
            "publication_year": 2019,
            "author": self.author1.id
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title="Book Three").publication_year, 2019)

    def test_create_book_unauthenticated(self):
        """Unauthenticated user cannot create a book"""
        data = {
            "title": "Book Four",
            "publication_year": 2018,
            "author": self.author2.id
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_invalid_publication_year(self):
        """Test validation prevents future publication_year"""
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "Future Book",
            "publication_year": 3000,
            "author": self.author1.id
        }

        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("publication_year", response.data)

    # ----------------------------
    # UPDATE TESTS
    # ----------------------------
    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username="testuser", password="testpass123")

        url = reverse("book-update", kwargs={"pk": self.book1.id})

        data = {
            "title": "Updated Book One"
        }

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_update_book_unauthenticated(self):
        """Unauthenticated user cannot update a book"""
        url = reverse("book-update", kwargs={"pk": self.book1.id})

        data = {
            "title": "Hack Update"
        }

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------
    # DELETE TESTS
    # ----------------------------
    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username="testuser", password="testpass123")

        url = reverse("book-delete", kwargs={"pk": self.book2.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_delete_book_unauthenticated(self):
        """Unauthenticated user cannot delete a book"""
        url = reverse("book-delete", kwargs={"pk": self.book2.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------------------
    # FILTERING TESTS
    # ----------------------------
    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url, {"title": "Book One"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_filter_books_by_publication_year(self):
        """Test filtering books by publication_year"""
        response = self.client.get(self.list_url, {"publication_year": 2021})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["publication_year"], 2021)

    # ----------------------------
    # SEARCH TESTS
    # ----------------------------
    def test_search_books(self):
        """Test searching books using SearchFilter"""
        response = self.client.get(self.list_url, {"search": "Two"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    # ----------------------------
    # ORDERING TESTS
    # ----------------------------
    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication_year descending"""
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2021)
        self.assertEqual(response.data[1]["publication_year"], 2020)
