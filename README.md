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
