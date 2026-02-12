from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title" ,"content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widget = {
           "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment here..."})

        }