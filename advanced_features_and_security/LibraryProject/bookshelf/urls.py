from django.urls import path
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
