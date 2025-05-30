# Django DRF with Google OAuth 2.0

This project implements a Django Rest Framework backend with Google OAuth 2.0 authentication and data management APIs.

## Features

- Google OAuth 2.0 Authentication
- Protected API endpoints
- Data entry and retrieval APIs
- Secure token handling

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with the following variables:
   ```
   SECRET_KEY=your_django_secret_key
   GOOGLE_CLIENT_ID=your_google_client_id
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   ```
5. Run migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/auth/google/` - Initiate Google OAuth flow
- `POST /api/auth/google/callback/` - Handle Google OAuth callback

### Data Management
- `POST /api/items/` - Create new item (requires authentication)
- `GET /api/items/` - List items (requires authentication)
- `GET /api/items/{id}/` - Get specific item (requires authentication)

## Google OAuth Setup

1. Go to Google Cloud Console
2. Create a new project
3. Enable Google OAuth 2.0 API
4. Create OAuth 2.0 credentials
5. Add authorized redirect URIs:
   - `http://localhost:8000/api/auth/google/callback/`
6. Copy Client ID and Client Secret to `.env` file

## Security Notes

- Never commit `.env` file
- Keep your Google OAuth credentials secure
- Use HTTPS in production
- Implement proper token refresh mechanism 