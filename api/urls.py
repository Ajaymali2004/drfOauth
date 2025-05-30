from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, GoogleOAuthViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/google/', GoogleOAuthViewSet.as_view({'get': 'auth', 'post': 'auth'}), name='google-auth'),
    path('auth/google/callback/', GoogleOAuthViewSet.as_view({'get': 'callback', 'post': 'callback'}), name='google-auth-callback'),
]