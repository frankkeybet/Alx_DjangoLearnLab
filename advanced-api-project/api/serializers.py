from rest_framework import serializers
from .models import Book , Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer
    --------------
    This serializer converts Book model instances into JSON format
    and validates incoming JSON data before saving it to the database.

    Validation:
    - Ensures publication_year is not greater than the current year
      (a book cannot be published in the future).
    """
    class Meta:
                model = Book
                fields = "__all__"

    def validate_publication_year(self,value):
            """Custom field validation for publication_year."""
            current_year = datetime.now().year
            
            if value > current_year:
                        raise serializers.ValidationError("publication year cannot be in future")
            return value
        
class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer
    ----------------
    This serializer converts Author instances into JSON format.

    Nested Serialization:
    - Includes the author's related books using BookSerializer.
    - The 'books' field uses the related_name='books' defined in Book model.
    - many=True means an author can have multiple books.
    - read_only=True ensures books are not directly created via AuthorSerializer.
    """
    books = BookSerializer(many=True ,read_only=True)

    class Meta:
           model= Author
           fields= ["id", "name", "books"]