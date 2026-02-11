from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view ,profile_view ,home_view,posts_view,post_detail_view

urlpatterns=[
    path("", home_view, name="home"),
    path("posts/", posts_view, name="posts"),
    path("posts/<int:post_id>/", post_detail_view, name="post_detail"),

    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
]