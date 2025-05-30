from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.conf import settings
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from .models import Item
from .serializers import ItemSerializer, UserSerializer

# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GoogleOAuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['get', 'post'])
    def auth(self, request):
        flow = Flow.from_client_config(
            {
                "web": {
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "client_secret": settings.GOOGLE_CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                }
            },
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
        )
        flow.redirect_uri = request.build_absolute_uri('/api/auth/google/callback/')
        url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        return Response({'authorization_url': url})

    @action(detail=False, methods=['get', 'post'])
    def callback(self, request):
        flow = Flow.from_client_config(
            {
                "web": {
                    "client_id": settings.GOOGLE_CLIENT_ID,
                    "client_secret": settings.GOOGLE_CLIENT_SECRET,
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                }
            },
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
        )
        flow.redirect_uri = request.build_absolute_uri('/api/auth/google/callback/')
        auth_response = request.build_absolute_uri()
        flow.fetch_token(authorization_response=auth_response)
        creds = flow.credentials
        service = build('oauth2', 'v2', credentials=creds)
        info = service.userinfo().get().execute()
        user, _ = User.objects.get_or_create(
            email=info['email'],
            defaults={
                'username': info['email'],
                'first_name': info.get('given_name', ''),
                'last_name': info.get('family_name', '')
            }
        )
        return Response({
            'user': UserSerializer(user).data,
            'access_token': creds.token,
            'refresh_token': creds.refresh_token
        })
