from rest_framework import authentication, exceptions
from django.contrib.auth.models import User
import requests

class GoogleAccessTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None

        token = auth_header.split(' ')[1]
        resp = requests.get('https://www.googleapis.com/oauth2/v3/userinfo', headers={'Authorization': f'Bearer {token}'})

        if resp.status_code != 200:
            raise exceptions.AuthenticationFailed('Invalid Google access token')

        info = resp.json()
        email = info.get('email')
        if not email:
            raise exceptions.AuthenticationFailed('No email found in Google userinfo')

        user, _ = User.objects.get_or_create(username=email, email=email)
        return (user, None)