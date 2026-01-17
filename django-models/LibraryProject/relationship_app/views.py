from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test


from django.contrib.auth.decorators import permission_required
from bookshelf.models import Book

from .models import Book
from .models import Library


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {
        'books': books
    })


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})



def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@permission_required('bookshelf.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')


@permission_required('bookshelf.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('bookshelf.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'relationship_app/delete_book.html', {'book': book})