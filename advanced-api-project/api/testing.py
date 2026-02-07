#run shell to tell author and books

from api.models import Author, Book
from api.serializers import AuthorSerializer, BookSerializer

# Create author
author = Author.objects.create(name="Chinua Achebe")

# Create books
book1 = Book.objects.create(title="Things Fall Apart", publication_year=1958, author=author)
book2 = Book.objects.create(title="No Longer at Ease", publication_year=1960, author=author)

# Serialize author (nested books should appear)
serializer = AuthorSerializer(author)
print(serializer.data)

#testing future year validation
bad_book = BookSerializer(data={
    "title": "Future Book",
    "publication_year": 2050,
    "author": author.id
})

bad_book.is_valid()
print(bad_book.errors)
