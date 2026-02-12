## Blog CRUD Features

Users can browse all posts using /posts/

Users can view a single post using /posts/<pk>/

Authenticated users can create posts using /posts/new/

Only post authors can edit posts using /posts/<pk>/edit/

Only post authors can delete posts using /posts/<pk>/delete/

## Security

CSRF protection included in all forms

Password hashing handled by Django

Access restricted using LoginRequiredMixin + UserPassesTestMixin


## Comment System

The blog includes a comment feature that allows users to interact with posts.

### Features
- Users can view comments under each blog post.
- Authenticated users can create comments.
- Only the author of a comment can edit or delete their comment.

### URLs
- Add Comment: /post/<post_id>/comment/new/
- Edit Comment: /comment/<comment_id>/update/
- Delete Comment: /comment/<comment_id>/delete/

### Security
- Comment creation requires authentication.
- Editing/deleting comments is restricted to the comment author.
- CSRF protection is enforced on all forms.
