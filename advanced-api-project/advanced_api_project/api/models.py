from django.db import models

# Create your models here.
class Author(models.Model):
     """
    Author Model
    ------------
    This model represents an author in the system.

    Fields:
    - name: Stores the full name of the author.

    Relationship:
    - One Author can have many Books (One-to-Many relationship).
      This relationship is defined through the Book model using a ForeignKey.
    """
     name = models.CharField(max_length=200)

     def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book Model
    ----------
    This model represents a book written by an author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: A ForeignKey relationship linking this book to an Author.

    Relationship:
    - Many books can belong to one author.
      (Each book has exactly one author.)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE ,related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
    