# Django Rest Framework with Google OAuth 2.0

This project implements a Django Rest Framework backend with Google OAuth 2.0 authentication and a Task Management API.

## Features

- Google OAuth 2.0 Authentication
- Task Management API (CRUD operations)
- Protected endpoints with user-specific data access
- Search functionality for tasks

## Prerequisites

- Python 3.8+
- Django 5.0+
- Google Cloud Platform account with OAuth 2.0 credentials

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with the following variables:
```
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/api/auth/google/callback/
SECRET_KEY=your_django_secret_key
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- `POST /api/google/login/` - Initiate Google OAuth login
- `GET /api/auth/google/callback/` - Google OAuth callback URL

### Tasks
- `GET /api/tasks/` - List all tasks for authenticated user
- `POST /api/tasks/` - Create a new task
- `GET /api/tasks/{id}/` - Retrieve a specific task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task
- `GET /api/tasks/search/?q={query}` - Search tasks by title

## Google OAuth Setup

1. Go to the Google Cloud Console
2. Create a new project
3. Enable the Google+ API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URIs
6. Copy the client ID and client secret to your `.env` file

## Security Considerations

- All endpoints are protected and require authentication
- User data is isolated and can only be accessed by the owner
- Sensitive credentials are stored in environment variables
- CSRF protection is enabled
- OAuth tokens are securely handled

## Testing the API

You can use Postman or any API client to test the endpoints:

1. First, authenticate using Google OAuth
2. Use the received access token in the Authorization header
3. Make requests to the task endpoints

Example task creation:
```json
POST /api/tasks/
{
    "title": "Sample Task",
    "description": "This is a sample task description"
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

# Django OAuth2 Project

This is a Django project with Google OAuth2 authentication, deployed on [Render.com](https://render.com).

---

## Features

- Google OAuth2 login
- CORS support enabled
- Environment variable configuration for security
- Ready for deployment with Gunicorn

---

## Environment Variables

Create a `.env` file (or configure environment variables on Render) with the following:

```env
SECRET_KEY=Your Django secret key

DEBUG=True

OAUTHLIB_INSECURE_TRANSPORT=1      
ALLOWED_HOSTS=localhost

CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_CREDENTIALS=True

GOOGLE_CLIENT_ID=Your Google OAuth credentials
GOOGLE_CLIENT_SECRET=Your Google OAuth credentials
