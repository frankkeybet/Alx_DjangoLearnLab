from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

from .forms import RegisterForm, ProfileUpdateForm

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Registration failed. Please enter valid details.")
    else:
        form = RegisterForm()

    return render(request, "blog/register.html", {"form": form})


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Update failed. Invalid details.")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})


def home_view(request):
    return render(request, "blog/home.html")

def posts_view(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/posts.html", {"posts": posts})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})