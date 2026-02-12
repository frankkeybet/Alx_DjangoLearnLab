from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment ,Tag


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
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas")

    class Meta:
        model = Post
        fields = ["title" ,"content", "tags"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields["tags"].initial = ", ".join(
                [tag.name for tag in self.instance.tags.all()]
            )

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()
        # Handle tags
        tags_str = self.cleaned_data.get("tags", "")
        tag_names = [t.strip() for t in tags_str.split(",") if t.strip()]

        post.tags.clear()
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)

        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widget = {
           "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment here..."})

        }