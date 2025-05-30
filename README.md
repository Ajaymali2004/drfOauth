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
git clone https://github.com/Ajaymali2004/drfOauth.git
cd drfOauth
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
SECRET_KEY=Your Django secret key

DEBUG=True

OAUTHLIB_INSECURE_TRANSPORT=1      
ALLOWED_HOSTS=localhost

CORS_ALLOW_ALL_ORIGINS=True
CORS_ALLOW_CREDENTIALS=True

GOOGLE_CLIENT_ID=Your Google OAuth credentials
GOOGLE_CLIENT_SECRET=Your Google OAuth credentials

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
