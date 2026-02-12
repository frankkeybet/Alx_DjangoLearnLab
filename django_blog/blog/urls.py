from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

from .views import (
    home_view,
    register_view,
    profile_view,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("search/", views.search_posts, name="search_posts"),
    path("tags/<str:tag_name>/", views.posts_by_tag, name="posts_by_tag"),

    # Blog CRUD (Checker Required)
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),

    # Comments
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment_new"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment_update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),


    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]
