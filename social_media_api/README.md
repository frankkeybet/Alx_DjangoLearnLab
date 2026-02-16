# Social Media API


## User Authentication

- **Register:** `POST /api/accounts/register/`
- **Login:** `POST /api/accounts/login/` (JWT tokens returned)
- **Profile:** JWT token required for protected endpoints

## User Model

- `username`, `email`, `password`
- `bio` – User biography
- `profile_picture` – User image
- `followers` – Users who follow this user


## Posts Endpoints

### List Posts
GET /api/posts/

### Create Post
POST /api/posts/
Authorization: Token <token>

Body:
{
  "title": "Hello",
  "content": "My content"
}

### Search Posts
GET /api/posts/?search=hello

---

## Comments Endpoints

### List Comments
GET /api/comments/

### Create Comment
POST /api/comments/
Authorization: Token <token>

