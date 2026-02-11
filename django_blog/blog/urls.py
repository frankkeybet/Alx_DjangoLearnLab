from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
    home_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register_view,
    profile_view,
)

urlpatterns = [
    path("", home_view, name="home"),

    # CRUD URLs
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/new/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
