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
